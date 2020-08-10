""" Cares urls """

# Django
from django.urls import path

# Views
from recoverid.cares.views import list_cares

urlpatterns = [
    path('cares/', list_cares),
]