from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Welcome to the Home Page!")

# Create your views here.
