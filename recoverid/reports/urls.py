from django.urls import path
from django.conf.urls import url

from recoverid.reports.views import uploadData, ReportsView

urlpatterns = [
    path('api/reports/', ReportsView.list_reports),
    path('api/reports/daily/<int:year>/<int:month>/<int:day>/',
         ReportsView.daily_report),
    path('reports/upload', uploadData),
    path('api/reports/countries/', ReportsView.reports_countries),
    path('api/reports/country/<str:code>/', ReportsView.report_country)
]
