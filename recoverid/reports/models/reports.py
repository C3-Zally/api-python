#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.countries.models import Country
from recoverid.states.models import State
from recoverid.cities.models import City

class Report(RecoveridModel):
    report_id = models.AutoField(primary_key=True)
    date = models.DateField(blank = True)
    infections = models.BigIntegerField()
    active_cases = models.BigIntegerField()
    new_cases = models.BigIntegerField()
    new_deaths = models.BigIntegerField()
    deaths = models.BigIntegerField()
    samples_proccesed = models.BigIntegerField()
    recovered  = models.BigIntegerField()
    country_id =models.ForeignKey(Country,on_delete=models.CASCADE) 
    state_id =models.ForeignKey(State,on_delete=models.CASCADE) 
    city_id =models.ForeignKey(City,on_delete=models.CASCADE)