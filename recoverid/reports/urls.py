from django.urls import path

from recoverid.reports.views import uploadData, list_reports

urlpatterns = [
    path('api/reports/', list_reports),
    path('reports/upload', uploadData),
]
