#Django
from django.db import models

from recoverid.utils.models import RecoveridModel
from recoverid.countries.models import Country
from recoverid.states.models import State
from recoverid.cities.models import City

TYPE_STATUS = [
    ("ACTIVE","ACTIVE"),
    ("INACTIVE","INACTIVE")
]
class Report(RecoveridModel):
    report_id = models.AutoField(primary_key=True)
    infections = models.BigIntegerField(null=True)
    active_cases = models.BigIntegerField(null=True)
    new_cases = models.BigIntegerField(null=True)
    new_deaths = models.BigIntegerField(null=True)
    deaths = models.BigIntegerField(null=True)
    samples_proccesed = models.BigIntegerField(null=True)
    recovered  = models.BigIntegerField(null=True)
    date = models.DateField(null = False,blank = False)
    country_id =models.ForeignKey(Country,on_delete=models.CASCADE, null=True) 
    state_id =models.ForeignKey(State,on_delete=models.CASCADE, null=True) 
    city_id =models.ForeignKey(City,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=8,choices=TYPE_STATUS)
    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on wich object was created.'

    )

    updated_at= models.DateTimeField(
        'updated at',
        auto_now = True,
        help_text='Date time on wich object was last updated.'

    )

    deleted_at= models.DateTimeField(
        'deleted at',
        auto_now_add=True,
        help_text='Date time on wich object was deleted.'

    )
