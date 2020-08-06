#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.utils.enums import StatusType

class City(RecoveridModel):
    """City Model"""
    city_id = models.AutoField(primary_key=True)
    cityt_name = models.CharField(max_length=50,required = True)
    state_id = models.ForeignKey("state.state_id",on_delete=CASCADE) 
    
    
    
