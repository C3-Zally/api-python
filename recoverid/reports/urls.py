from django.urls import path
from django.conf.urls import url

from recoverid.reports.views import uploadData, ReportsView

urlpatterns = [
    path('api/reports/', ReportsView.list_reports),
    path('api/reports/daily/<int:year>/<int:month>/<int:day>/', ReportsView.daily_report),
    path('reports/upload', uploadData),
    path('api/reports/countries/', ReportsView.reports_countries),
    path('api/reports/country/<str:code>/', ReportsView.report_country),
    path('api/reports/country/<str:code>/from/<int:y1>/<int:m1>/<int:d1>/to/<int:y2>/<int:m2>/<int:d2>/', ReportsView.reports_from_to)
]
