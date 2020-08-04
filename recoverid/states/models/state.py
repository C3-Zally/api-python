#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.utils.enums import StatusType

class State(RecoveridModel):
    """State Model"""
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50,required = True)
    latitude = models.FloatField
    longitude = models.FloatField
    country_id = models.ForeignKey("country.country_id",on_delete=CASCADE) 
    flag  =  models.CharField(max_length=500)
    population = models.BigIntegerField
    status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])
