#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.states.models import State

class City(RecoveridModel):
    """City Model"""
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50, blank = True)
    country_id = models.ForeignKey(State,on_delete=models.CASCADE) 
    flag  =  models.CharField(max_length=500)
    population = models.BigIntegerField()

    def __str__(self):
        """ return city name """
        return self.city_name
