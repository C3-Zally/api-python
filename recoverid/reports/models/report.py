#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.utils.enums import StatusType

class Reports (RecoveridModel):
    report_id = models.AutoField(primary_key=True)
    date = models.DateField(required = True)
    infections = models.BigIntegerField
    active_cases = models.BigIntegerField
    new_cases = models.BigIntegerField
    new_deaths = models.BigIntegerField
    deaths = models.BigIntegerField
    samples_proccesed = models.BigIntegerField
    recovered  = models.BigIntegerField
    country_id =models.ForeignKey("country.country_id",on_delete=CASCADE) 
    state_id =models.ForeignKey("state.state_id",on_delete=CASCADE) 
    city_id =models.ForeignKey("city.city_id",on_delete=CASCADE) 
    status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])