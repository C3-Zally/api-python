"""Django models utilities"""

#Django
from django.db import models


class RecoveridModel(models.Model):
    """Recoverid Model"""

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
        help_text='Date time on wich object was deleted.'

    )

    latitude = models.FloatField
    longitude = models.FloatField
    status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])
    population = models.BigIntegerField
    flag  =  models.CharField(max_length=500)