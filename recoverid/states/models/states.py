#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
# from recoverid.utils.enums import StatusType
from recoverid.countries.models import Country

class State(RecoveridModel):
    """State Model"""
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50,blank = True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE) 
    flag  =  models.CharField(max_length=500)
    population = models.BigIntegerField()
    # status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])

    def __str__(self):
        """ return id """
        return self.state_id
