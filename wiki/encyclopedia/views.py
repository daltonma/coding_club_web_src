from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wiki(request, title):
    return HttpResponse(f"You're looking at the wiki page for {title}.")

def index(request):
    return HttpResponse("Not Yet Implemented. <br/><img src='https://http.cat/501' alt='Too Early HTTP Status Cat'>", status=501)