from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf

from datagen.models import *


# search using post
def search_post(request):
    ctx = {}
    if request.POST:
        check_list = request.POST.getlist('check_list')

        # search in database
        # Example of select: country_result = Country.objects.get(countryCode=para[2])
        country_all = Country.objects.all()

        ctx['rlt'] = ""

        if "name" in check_list:
            ctx['rlt'] += "Name Selected!" + "<br/>"
            # TODO: select name from database

        if "gender" in check_list:
            ctx['rlt'] += "Gender Selected!" + "<br/>"
            gender = request.POST['gender']
            # TODO: select gender from database

        if "country" in check_list:
            ctx['rlt'] += "Country Selected!" + "<br/>"
            country = request.POST['country']
            # TODO: select country from database

        if "race" in check_list:
            ctx['rlt'] += "Race Selected!" + "<br/>"
            race = request.POST['race']
            # TODO: select race from database

        if "address" in check_list:
            ctx['rlt'] += "Address Selected!" + "<br/>"
            # TODO: select address from database

        for item in country_all:
            ctx['rlt'] += (item.countryCode + " " + item.countryName) + "<br/>"

    return render(request, "generate.html", ctx)
