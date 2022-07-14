from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name=_('Name'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))

    def __str__(self) -> str:
        return self.name
