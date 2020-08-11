#Django
from django.db import models

from recoverid.utils.models import RecoveridModel


class City(RecoveridModel):
    """City Model"""
    city_id = models.AutoField(primary_key=True)
    cityt_name = models.CharField(max_length=50,null = False,blank = False)
    state_id = models.ForeignKey("states.State",on_delete=models.CASCADE) 
    
    
    
