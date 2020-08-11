#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
<<<<<<< HEAD
# from recoverid.utils.enums import StatusType
from recoverid.countries.models import Country
=======
>>>>>>> features

class State(RecoveridModel):
    """State Model"""
    state_id = models.AutoField(primary_key=True)
<<<<<<< HEAD
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
=======
    state_name = models.CharField(max_length=50,null = False,blank = False)
    country_id = models.ForeignKey("countries.Country",on_delete=models.CASCADE) 
    
    
    
>>>>>>> features
