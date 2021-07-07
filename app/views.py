from django.shortcuts import render


# Create your views here.
def initial_form(request):
    return render(request, "app/initial-form.html", {

    })


def grid(request):
    return render(request, "app/grid.html")
