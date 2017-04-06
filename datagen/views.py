from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Data Generator Page")

def manual(request):
    return HttpResponse("User Manual Page")

def documentation(request):
    return HttpResponse("Documentation Page")
