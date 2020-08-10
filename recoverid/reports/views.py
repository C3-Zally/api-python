""" Reports views """

# Django REST Framework
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Django
from django.db.models import Sum

# Models
from recoverid.reports.models import Report

@api_view()
@renderer_classes([JSONRenderer])
def list_reports(self):
    """ List reports """
    reports = Report.objects.all()
    data = []
    confirm = Report.objects.all().aggregate(Sum('infections'))
    confirmed = confirm['infections__sum']
    dead = Report.objects.all().aggregate(Sum('deaths'))
    deaths = dead['deaths__sum']
    recover = Report.objects.all().aggregate(Sum('recovered'))
    recovered = recover['recovered__sum']
    for report in reports:
        data.append({
            'Last_updated': report.date,
            'confirmed': confirmed,
            'active_cases': report.active_cases,
            'deaths': deaths,
            'Last_modified': report.updated_at,
            'recovered': recovered,
        })
    return Response(data, status=200)