from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf
from django.db import connection

from datagen.models import *
from random import randint, random
import copy
import parser
from Dataset import Dataset
import itertools


# search using post
def search_post(request):
    display = []

    # Pre-processing at parser module
    dataset = parser.read_request(request)

    # Build Query from Indicator ind
    datasets = []
    names = []
    genders = []
    countries = []
    races = []
    addresses = []
    ccards = []

    limit = dataset.get_rows()
    query_limit = " ORDER BY random() LIMIT " + str(limit) + ";"
    if limit > 0:
        # Name --> Gender, Country, Race
        if dataset.get_names()[0]:
            query_select = "SELECT firstName, lastName"
            query_from = " FROM FirstName, LastName"
            query_where = " WHERE FirstName.raceId = LastName.raceId"
            query = query_select + query_from + query_where + query_limit
            result = execute(query, 2)
            # form name
            for i in range(0, len(result[0])):
                names.append(str(result[0][i]) + " " + str(result[1][i]))
        if dataset.get_gender()[0]:
            query_select = "SELECT genderDesc"
            query_from = " FROM Gender"
            query_where = ""
            query = query_select + query_from + query_where + query_limit
            genders.append(execute(query, 1))
        if dataset.get_country()[0]:
            query_select = "SELECT countryName"
            query_from = " FROM Country"
            query_where = ""
            query = query_select + query_from + query_where + query_limit
            countries.append(execute(query, 1))
        if dataset.get_race()[0]:
            query_select = "SELECT raceDesc"
            query_from = " FROM Race"
            query_where = ""
            query = query_select + query_from + query_where + query_limit
            races.append(execute(query, 1))
        if dataset.get_address()[0] :
            query_select = "SELECT addressDesc, countryName, postalCode"
            query_from = " FROM Address, Country"
            query_where = " WHERE Address.countryCode = Country.countryCode"
            query = query_select + query_from + query_where + query_limit
            result = execute(query, 3)
            # form address
            for i in range(0, len(result[0])):
                addresses.append(str(result[0][i]) + ", " + str(result[1][i]) + "  " + str(result[2][i]))
        if dataset.get_cc()[0]:
            query_select = "SELECT prefix"
            query_from = " FROM CCCompany"
            query_where = ""
            query = query_select + query_from + query_where + query_limit
            ccards.append(execute(query, 1))

    # Randomize based on statistics distribution

    # Convert into list of dict where each dict = 1 record
    display = []
    for i in range(0, limit):
        record = dict()
        if dataset.get_names()[0]:
            record["Names"] = names[i % len(names)]
        if dataset.get_gender()[0]:
            record["Gender"] = genders[i % len(genders)]
        if dataset.get_country()[0]:
            record["Country"] = countries[i % len(countries)]
        if dataset.get_race()[0]:
            record["Race"] = races[i % len(races)]
        if dataset.get_address()[0]:
            record["Address"] = addresses[i % len(addresses)]
        if dataset.get_cc()[0]:
            record["CreditCard"] = ccards[i % len(ccards)]
        display.append(record)
    # # Add records to display until target length is reached
    # if len(display) > dataset.get_rows():
    #     del display[dataset.get_rows():]
    return render(request, "generate.html", {'datas': display})


# Executes SQL Query on DB, returns list of values (without header)
def execute(query, num_cols):
    result = []
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            for r in range(0, num_cols):
                result.append(row[r])
    finally:
        cursor.close()
    return result


def digits_of(number):
    return [int(i) for i in str(number)]


def luhn_checksum(partial_card):
    odd_digits = partial_card[-1::-2]
    even_digits = partial_card[-2::-2]
    total = sum(digits_of(odd_digits))
    for digit in even_digits:
        total += sum(2 * (digits_of(digit)))
    return str((9 * total) % 10)


# def generate_credit_card_num(credit_card_obj):
#     credit_card = random.choice(credit_card_obj)
#     prefix = str(credit_card.prefix)
#     credit_card_num_array = list(prefix)
#     length = credit_card.length
#     lengthLeft = length - len(prefix) - 1
#     for index in range(0, int(lengthLeft)):
#         credit_card_num_array.append(str(randint(0, 9)))
#
#     credit_card_num_array.append(luhn_checksum(ccn))
#     credit_card_num = ''.join(credit_card_num_array)
#    return credit_card_num