from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe


class NewGameForm(forms.Form):
    columns = forms.IntegerField(label=mark_safe('columns'))
    rows = forms.IntegerField(label=mark_safe('<br/>rows'))
    generations = forms.IntegerField(label=mark_safe('<br/>generations'))


# Create your views here.
def initial_form(request):
    if request.method == "POST":
        form = NewGameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.session["grid_data"] = data
        return HttpResponseRedirect(reverse("grid"))
    else:
        return render(request, "app/initial-form.html", {
            "initial_form": NewGameForm()
        })


def grid(request):
    if "grid_data" not in request.session:
        request.session["grid_data"] = []
    return render(request, "app/grid.html", {
        "grid_data": request.session["grid_data"]
    })
