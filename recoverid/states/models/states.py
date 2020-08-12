#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.countries.models import Country

class State(RecoveridModel):
    """State Model"""
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50,null = False,blank = False)
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        """ return id """
        return self.state_id
    
    
    
    
