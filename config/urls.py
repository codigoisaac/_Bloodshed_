from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django! This is the Home Page.")


def room(request):
    return HttpResponse("This is the secret room.")


urlpatterns = [path("admin/", admin.site.urls), path("", home), path("room/", room)]
