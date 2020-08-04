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