#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.utils.enums import StatusType

class Country(RecoveridModel):
    """Contry Model"""
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50,required= True)
    alpha2code = models.CharField(max_length=5)
    alpha3code = models.CharField(max_length=5)
    capital =  models.CharField(max_length=50)
    region =  models.CharField(max_length=50)
    subregion  =  models.CharField(max_length=50)
    latitude = models.FloatField
    longitude = models.FloatField
    flag  =  models.CharField(max_length=500)
    population = models.BigIntegerField
    status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])