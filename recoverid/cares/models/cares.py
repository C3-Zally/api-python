# Django
from django.db import models

# Utilites
from recoverid.utils.models import RecoveridModel

class Care(RecoveridModel):
    """Care Model"""
    care_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    