from django.utils.translation import LANGUAGE_SESSION_KEY
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf
from django.db import connection

from datagen.models import *
from random import randint, random
import copy
from Dataset import Dataset
import itertools
import decimal

# Pre-defined parameters
MAX_ROWS = 1000


# search using post
def search_post(request):
    display = []

    # Pre-processing at parser module
    dataset = Dataset()

    if request.POST:
        check_list = request.POST.getlist('check_list')

        if request.POST['rows']:
            rows = to_int(request.POST['rows'])
            if validate_rows(rows):
                dataset.set_rows(rows)
            # else use default value, rows = 100
        if "name" in check_list:
            dataset.set_names()
        if "gender" in check_list:
            if "male_percent" in check_list and "female_percent" in check_list:
                male_percent = to_int(request.POST['male_percent'])
                female_percent = to_int(request.POST['female_percent'])
                if validate_percentage(male_percent, female_percent):
                    dataset.set_gender(male_percent, 100 - male_percent)
            else:  # use default value, 50% male, 50% female
                dataset.set_gender(50, 50)
        if "country" in check_list:
            country_name_1 = request.POST['country_name_1']
            country_name_2 = request.POST['country_name_2']
            temp1 = request.POST['country_percent_1']
            temp2 = request.POST['country_percent_2']
            if temp1 != "" and temp2 != "":
                country_percent_1 = to_int(temp1)
                country_percent_2 = to_int(temp2)
                if validate_percentage(temp1, temp2) and country_name_1 != country_name_2:
                    dataset.set_country(country_name_1, country_percent_1, country_name_2, country_percent_2)
                else:
                    dataset.set_country("No Preference", 100, "No Preference", 0)
            else:
                dataset.set_country("No Preference", 100, "No Preference", 0)

        if "race" in check_list:
            race_name_1 = request.POST['race_name_1']
            race_name_2 = request.POST['race_name_2']
            temp1 = request.POST['race_percent_1']
            temp2 = request.POST['race_percent_2']
            if temp1 != "" and temp2 != "":
                race_percent_1 = to_int(temp1)
                race_percent_2 = to_int(temp2)
                if validate_percentage(temp1, temp2) and race_name_1 != race_name_2:
                    dataset.set_race(race_name_1, race_percent_1, race_name_2, race_percent_2)
                else:
                    dataset.set_race("No Preference", 100, "No Preference", 0)
            else:
                dataset.set_race("No Preference", 100, "No Preference", 0)
        if "address" in check_list:
            dataset.set_address()
        if "credit_card" in check_list:
            cc_name_1 = request.POST['cc_name_1']
            cc_name_2 = request.POST['cc_name_2']
            temp1 = request.POST['cc_percent_1']
            temp2 = request.POST['cc_percent_2']
            if temp1 != "" and temp2 != "":
                cc_percent_1 = to_int(temp1)
                cc_percent_2 = to_int(temp2)
                if validate_percentage(temp1, temp2) and cc_name_1 != cc_name_2:
                    dataset.set_cc(cc_name_1, cc_percent_1, cc_name_2, cc_percent_2)
                else:
                    dataset.set_cc("No Preference", 100, "No Preference", 0)
            else:
                dataset.set_cc("No Preference", 100, "No Preference", 0)

        # Build Query from Dataset's dataset
        names = []
        genders = []
        countries = []
        races = []
        addresses = []
        ccards = []

        limit = dataset.get_rows()
        query_limit = " ORDER BY random() LIMIT " + str(limit) + ";"
        if limit > 0:
            if dataset.get_names()[0]:
                query_select = "SELECT firstName, lastName"
                query_from = " FROM FirstName, LastName"
                query_where = " WHERE FirstName.raceId = LastName.raceId"
                query = query_select + query_from + query_where + query_limit
                result = execute(query, 2)
                # form name
                if result != [[]]:
                    for i in range(0, len(result)):
                        names.append((result[i][0]) + " " + (result[i][1]))
                else:
                    dataset.names = [False]
            if dataset.get_gender()[0]:
                query_select = "SELECT genderDesc"
                query_from = " FROM Gender"
                query_where = ""
                query = query_select + query_from + query_where + query_limit
                genders = execute(query, 1)
            if dataset.get_country()[0]:
                query_select = "SELECT countryName"
                query_from = " FROM Country"
                # if dataset.get_country()[1] == "Malaysia":
                #     query_where = " WHERE countryName = 'Malaysia'"
                if dataset.get_country()[1] != "No Preference":
                    query_where = " WHERE countryName = '" + dataset.get_country()[1] + "'"
                else:
                    query_where = ""
                query = query_select + query_from + query_where + query_limit
                countries = execute(query, 1)
                print "countries = ", countries
            if dataset.get_race()[0]:
                query_select = "SELECT raceDesc"
                query_from = " FROM Race"
                if dataset.get_race()[1] != "No Preference":
                    query_where = " WHERE raceDesc = '" + dataset.get_race()[1] + "'"
                else:
                    query_where = ""
                query = query_select + query_from + query_where + query_limit
                races = execute(query, 1)
            if dataset.get_address()[0]:
                query_select = "SELECT addressDesc, countryName, postalCode"
                query_from = " FROM Address, Country"
                query_where = " WHERE Address.countryCode = Country.countryCode"
                query = query_select + query_from + query_where + query_limit
                result = execute(query, 3)
                # form address
                if result != [[]]:
                    for i in range(0, len(result)):
                        addresses.append((result[i][0]) + ", " + (result[i][1]) + " " + (result[i][2]))
                else:
                    dataset.addresses = [False]
            if dataset.get_cc()[0]:
                query_select = "SELECT prefix, len"
                query_from = " FROM CCCompany"
                query_where = ""
                query = query_select + query_from + query_where + query_limit
                results = execute(query, 2)

                # form credit card number
                if results != [[]]:
                    for i in range(0, len(results)):
                        prefix = to_int(results[i][0])
                        length = to_int(results[i][1])
                        ccards.append(generate_credit_card_num(prefix, length))

        # Randomize based on statistics distribution

        # Convert into list of dict where each dict = 1 record
        display = convert_to_dict(addresses, ccards, countries, dataset, genders, limit, names, races)
        # # Add records to display until target length is reached

    return render(request, "generate.html", {'datas': display})


# Converts each record into a dictionary and returns a list of dictionaries
def convert_to_dict(addresses, ccards, countries, dataset, genders, limit, names, races):
    display = []
    for i in range(0, limit):
        record = dict()
        if dataset.get_names()[0]:
            record["Name"] = names[i % len(names)]
            # print record["Name"]
        if dataset.get_gender()[0]:
            record["Gender"] = genders[i % len(genders)]
            # print record["Gender"]
        if dataset.get_country()[0]:
            record["Country"] = countries[i % len(countries)]
            # print record["Country"]
        if dataset.get_race()[0]:
            record["Race"] = races[i % len(races)]
            # print record["Race"]
        if dataset.get_address()[0]:
            record["Address"] = addresses[i % len(addresses)]
            # print record["Address"]
        if dataset.get_cc()[0]:
            record["CreditCard"] = ccards[i % len(ccards)]
            # print record["CreditCard"]
        display.append(record)
    return display


# Converts string to int with rounding as required
def to_int(value):
    return int(round(decimal.Decimal(str(value))))


# Validates rows fall within valid range of values
def validate_rows(rows):
    if 0 < rows <= MAX_ROWS:
        return True
    else:
        return False


# Validate percentage pairs
def validate_percentage(percent_1, percent_2):
    # Check sum = 100% and no negative values
    sum = to_int(percent_1) + to_int(percent_2)
    if sum == 100 and percent_1 > 0 and percent_2 > 0:
        return True
    else:
        return False


# Executes SQL Query on DB, returns list of values (without header)
def execute(query, num_cols):
    result = []
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        if num_cols > 1:
            for row in cursor.fetchall():
                record = []
                for r in range(0, num_cols):
                    record.append(row[r])
                result.append(record)
        elif num_cols == 1:
            for row in cursor.fetchall():
                result.append(str(row[0]))

    finally:
        cursor.close()
    return result

# Converts string number to int
def digits_of(number):
    return [int(i) for i in number]


# Luhn's algorithm to generate check-digit
def luhn_checksum(partial_card):
    odd_digits = partial_card[-1::-2]
    even_digits = partial_card[-2::-2]
    total = sum(digits_of(odd_digits))
    for digit in even_digits:
        total += sum(2 * (digits_of(digit)))
    return str((9 * total) % 10)


# Generates credit card numbers from (int) prefix and (int) length
def generate_credit_card_num(prefix, length):
    credit_card_num_array = list(str(prefix))
    length_left = length - len(str(prefix)) - 1
    for index in range(0, int(length_left)):
        credit_card_num_array.append(str(randint(0, 9)))
    credit_card_num_array.append(luhn_checksum(credit_card_num_array))
    credit_card_num = ''.join(credit_card_num_array)
    return credit_card_num
