"""Django models utilities"""

# Django
from django.db import models


TYPE_STATUS = [
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE")
]


class RecoveridModel(models.Model):
    """Recoverid Base Model

    RecoveridModel is the abstact base class for every
    models that can be created in this project.
    """
    population = models.IntegerField
    flag = models.CharField(max_length=500)
    latitude = models.FloatField
    longitude = models.FloatField
    #status = models.CharField(max_length=8,choices=[(tag, tag.value) for tag in StatusType])
    status = models.CharField(max_length=8, choices=TYPE_STATUS)

    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which object was created.'
    )

    updated_at = models.DateTimeField(
        'updated at',
        auto_now=True,
        help_text='Date time on which object was last updated.'
    )

    deleted_at = models.DateTimeField(
        'deleted at',
        auto_now_add=True,
        help_text='Date time on wich object was deleted.'
    )


    class Meta:
        """Meta option."""
        abstract = True
