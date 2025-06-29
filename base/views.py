from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django! This is the Home Page.")


def room(request):
    return HttpResponse("This is the secret room.")
