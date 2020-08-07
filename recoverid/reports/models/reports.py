#Django
from django.db import models


from recoverid.utils.enums import StatusType


TYPE_STATUS = [
        ("ACTIVE","ACTIVE"),
        ("INACTIVE","INACTIVE")
        ]


class Report():
    report_id = models.AutoField(primary_key=True)
    date = models.DateField(null = False,blank = False)
    infections = models.BigIntegerField
    active_cases = models.BigIntegerField
    new_cases = models.BigIntegerField
    new_deaths = models.BigIntegerField
    deaths = models.BigIntegerField
    samples_proccesed = models.BigIntegerField
    recovered  = models.BigIntegerField
    country_id =models.ForeignKey("countries.Country",on_delete=models.CASCADE) 
    state_id =models.ForeignKey("states.State",on_delete=models.CASCADE) 
    city_id =models.ForeignKey("cities.City",on_delete=models.CASCADE) 
    #status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])
    status = models.CharField(max_length=8,choices=TYPE_STATUS)
    reated_at = models.DateTimeField(
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
        help_text='Date time on wich object was deleted.'

    )