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