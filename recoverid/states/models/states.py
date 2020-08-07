#Django
from django.db import models

from recoverid.utils.models import RecoveridModel

class State(RecoveridModel):
    """State Model"""
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50,null = False,blank = False)
    country_id = models.ForeignKey("countries.Country",on_delete=models.CASCADE) 
    
    
    
