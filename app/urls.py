from django.urls import path
from . import views

urlpatterns = [
    path("", views.initial_form, name="initial_form")
]