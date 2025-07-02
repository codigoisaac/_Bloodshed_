from django.shortcuts import render

rooms = [
    {"id": 1, "name": "Let's learn Python!"},
    {"id": 2, "name": "Let's learn Angular!"},
    {"id": 3, "name": "Let's learn Goang!"},
    {"id": 4, "name": "Let's learn C#!"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request):
    return render(request, "base/room.html")
