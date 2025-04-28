from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")


def name(request, name):
    return HttpResponse("Hello, " + name + "!")


def templated_name(request, name):
    return render(request, "greet/name.html", {"name": name})