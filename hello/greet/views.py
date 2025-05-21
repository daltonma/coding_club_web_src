from django.shortcuts import render, HttpResponse
from datetime import date

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")


def name(request, name):
    return HttpResponse("Hello, " + name + "!")


def templated_name(request, name):
    return render(request, "greet/name.html", {"name": name})


def christmas(request):
    date_today = date.today()
    todayischristmas = date_today.month == 12 and date_today.day == 25
    return render(
        request,
        "greet/christmas.html",
        {
            "today": date_today.today(),
            "todayischristmas": todayischristmas,
            "days_until_christmas": 0
            if todayischristmas
            else (date(2023, 12, 25) - date_today).days,
        },
    )
