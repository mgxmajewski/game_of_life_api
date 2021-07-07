from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewGameForm(forms.Form):
    columns = forms.IntegerField(label="columns")
    rows = forms.IntegerField(label="rows")
    generations = forms.IntegerField(label="generations")


grid_data = []


# Create your views here.
def initial_form(request):
    return render(request, "app/initial-form.html", {

    })


def grid(request):
    return render(request, "app/grid.html")
