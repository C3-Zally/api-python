from django.urls import path

from recoverid.reports.views import uploadData

urlpatterns = [
    path('reports/upload',uploadData)
]
