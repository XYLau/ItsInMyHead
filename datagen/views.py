from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Data Generator Page")

def manual(request):
    return render(request, "manual.html")

def documentation(request):
    return render(request, "documentation.html")
