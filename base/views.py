from django.shortcuts import render

rooms = [
    {"id": 1, "slug": "python", "name": "Python", "message": "Let's learn Python!"},
    {"id": 2, "slug": "angular", "name": "Angular", "message": "Let's learn Angular!"},
    {"id": 3, "slug": "go", "name": "Go", "message": "Let's learn Go!"},
    {"id": 4, "slug": "csharp", "name": "C#", "message": "Let's learn C#!"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, slug):
    room = None
    for i in rooms:
        if i["slug"] == str(slug):
            room = i

    context = {"room": room}

    return render(request, "base/room.html", context)
