""" Countries urls """

# Django
from django.urls import path

# Views
from recoverid.countries.views import list_countries

urlpatterns = [
    path('api/country/', list_countries),
]