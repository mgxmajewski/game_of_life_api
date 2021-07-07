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
    if request.method == "POST":
        form = NewGameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            grid_data.append(data)
        return HttpResponseRedirect(reverse("grid"))
    else:
        return render(request, "app/initial-form.html", {
            "initial_form": NewGameForm()
        })


def grid(request):
    return render(request, "app/grid.html", {
        "grid_data": grid_data
    })
