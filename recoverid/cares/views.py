""" Cares views """

# Django REST Framework
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Models
from recoverid.cares.models import Care

@api_view()
@renderer_classes([JSONRenderer])
def list_cares(self):
    """ List Cares """
    cares = Care.objects.all()
    data = []
    for care in cares:
        data.append({
            'care_id': care.care_id,
            'title': care.title,
            'slug': care.slug,
            'description': care.description
        })
    return Response(data, status=200)

@api_view()
@renderer_classes([JSONRenderer])
def list_apis(self):
    """ List of apis """
    data = [
        {
            "countries": "http://localhost:8000/api/country/",
            "totals": "http://localhost:8000/api/reports/",
            # "totalsByDay": "http://localhost/api/report/daily?date=2020-08-04",
            # "latestAllCountries": "http://localhost/api/report/countries",
            # "latestCountriesByCode": "http://localhost/api/report/countries?code=CO"
        }
    ]
    return Response(data, status=200)