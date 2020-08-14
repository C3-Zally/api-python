""" Cares urls """

# Django
from django.urls import path

# Views
from recoverid.cares.views import list_cares, list_apis

urlpatterns = [
    path('cares/', list_cares),
    path('', list_apis)
]
