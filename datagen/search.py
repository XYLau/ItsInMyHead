from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf

from datagen.models import *


# search using post
def search_post(request):
    ctx = {}
    para = {}
    if request.POST:
        para[1] = request.POST['country']
        para[2] = request.POST['code']

        # search in database
        country_result = Country.objects.get(countryCode=para[2])

        # value to display in generate.html
        ctx['rlt'] = country_result.countryCode + " " + country_result.countryName
    return render(request, "generate.html", ctx)
