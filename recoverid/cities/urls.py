""" Cities urls """

# Django
from django.urls import path

# Views
from recoverid.cities.views import list_cities

urlpatterns = [
    path('api/countries/cities', list_cities)
]