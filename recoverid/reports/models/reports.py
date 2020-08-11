#Django
from django.db import models

TYPE_STATUS = [
        ("ACTIVE","ACTIVE"),
        ("INACTIVE","INACTIVE")
        ]


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    date = models.DateField(null = False,blank = False)
    infections = models.IntegerField(null=True) 
    active_cases = models.IntegerField(null=True)
    new_cases = models.IntegerField(null=True)
    new_deaths = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    samples_proccesed = models.IntegerField(null=True)
    recovered  = models.IntegerField(null=True)
    country_id =models.ForeignKey("countries.Country",on_delete=models.CASCADE, null=True) 
    state_id =models.ForeignKey("states.State",on_delete=models.CASCADE, null=True) 
    city_id =models.ForeignKey("cities.City",on_delete=models.CASCADE, null=True) 
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
        auto_now_add=True,
        help_text='Date time on wich object was deleted.'

    )