from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def initial_form(request):
    return HttpResponse("Test!")
