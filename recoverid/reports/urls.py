<<<<<<< HEAD
""" Reports urls """

# Django
from django.urls import path

# Views
from recoverid.reports.views import list_reports

urlpatterns = [
    path('api/reports/', list_reports)
]
=======
from django.urls import path

from recoverid.reports.views import uploadData

urlpatterns = [
    path('reports/upload',uploadData)
]
>>>>>>> features
