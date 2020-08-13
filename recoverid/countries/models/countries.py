# Django
from django.db import models

from recoverid.utils.models import RecoveridModel


class Country(RecoveridModel):
    """Contry Model"""
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50, null=False, blank=False)
    alpha2code = models.CharField(max_length=5)
    alpha3code = models.CharField(max_length=5)
    capital = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    subregion = models.CharField(max_length=50)
    # population = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        """ Return country name """
        return self.country_name
