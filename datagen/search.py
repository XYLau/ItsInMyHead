from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf
from django.db import connection

from datagen.models import *
import copy
import itertools
from random import randint

# search using post
def search_post(request):
    display = []
    if request.POST:
        check_list = request.POST.getlist('check_list')
        # default set 100 rows of data
        rows = 100
        if request.POST['rows']:
            rows = int(request.POST['rows'])

        # deal with gender filter
        if "gender" in check_list:
            # display.append("Gender Selected!")
            gender = request.POST['gender']

        # deal with country filter
        if "country" in check_list:
            # display.append("Country Selected!")
            country = request.POST['country']
            if country:
                country_obj = Country.objects.filter(countryName=country)
            else:
                country_obj = Country.objects.all()

        # race filter
        if "race" in check_list:
            # display.append("Race Selected!")
            race = request.POST['race']
            if race:
                race_obj = Race.objects.get(raceDesc=race)

        if "name" in check_list:
            # display.append("Name Selected!")
            first_name_obj = FirstName.objects.all()
            last_name_obj = LastName.objects.all()

        if "address" in check_list:
            display.append("Address Selected!")
            # TODO: select. wait until address model complete
            
        # Credit Card 
        if "credit_card" in check_list:
            credit_card_obj = CCCompany.objects.all()

        # Select from db

        # if name is selected
        if "name" in check_list:
            if "race" in check_list and race:
                first_name_obj = first_name_obj.filter(raceId_id=race_obj.raceId)
            if "gender" in check_list and gender:
                first_name_obj = first_name_obj.filter(gender=gender)
            for item_first in first_name_obj:
                race_id = item_first.raceId_id

                for item_last in last_name_obj.filter(raceId_id=race_id):
                    attr = dict()
                    # attr['FirstName'] = item_first.firstName
                    # attr['LastName'] = item_last.lastName
                    attr['Name'] = item_first.firstName + " " + item_last.lastName

                    if "race" in check_list:
                        attr['Race'] = Race.objects.get(raceId=race_id).raceDesc
                    if "gender" in check_list:
                        attr['Gender'] = item_first.gender

                    if "address" in check_list:
                        # TODO : finish address generate
                        attr['Address'] = "Address"
                        
                    # for credit card --> not sure correct not
                    if "credit_card" in check_list:
                        attr["CreditCard"] = generate_credit_card_num(credit_card_obj)

                    if "country" in check_list:
                        for item_country in country_obj:
                            attr_country = copy.copy(attr)
                            attr_country['CountryName'] = item_country.countryName
                            attr_country['CountryCode'] = item_country.countryCode
                            display.append(attr_country)
                    else:
                        display.append(attr)

        if len(display) > rows:
            del display[rows:]

    return render(request, "generate.html", {'datas': display})

def joinNames(arr1, arr2, limit):
    result = dict()
    names = []
    count = 0
    isLimit = False

    while (isLimit == False):
        for r in itertools.product(arr1, arr2):
            if count < limit:
                newName = str(r[0]) + str(r[1])
                names.append(newName)
                print "count = ", count,", name = ", newName
                count += 1
            else:
                isLimit = True
                break
    result["Name"] = names
    return result

                                   
def digits_of(number):
    return [int(i) for i in str(number)]

def luhn_checksum(partial_card):
    odd_digits = partial_card[-1::-2]
    even_digits = partial_card[-2::-2]
    total = sum(digits_of(odd_digits))
    for digit in even_digits:
        total += sum(2*(digits_of(digit)))
    return str((9 * total) % 10)                               

def generate_credit_card_num(credit_card_obj):
    credit_card = random.choice(credit_card_obj)
    prefix = str(credit_card.prefix)
    credit_card_num_array = list(prefix)
    length = credit_card.length
    lengthLeft = length - len(prefix) - 1
    for index in range(0, int(lengthLeft)):
        credit_card_num_array.append(str(randint(0,9)))
                
    credit_card_num_array.append(luhn_checksum(ccn))
    credit_card_num = ''.join(credit_card_num_array)
    return credit_card_num