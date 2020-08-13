#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.states.models import State


class City(RecoveridModel):
    """City Model"""
    city_id = models.AutoField(primary_key=True)
    cityt_name = models.CharField(max_length=50,null = False,blank = False)
    state_id = models.ForeignKey(State,on_delete=models.CASCADE) 
    
    
    def __str__(self):
        """ return city name """
        return self.city_name

