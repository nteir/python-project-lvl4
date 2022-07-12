from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class TaskStatus(models.Model):
    name = models.CharField(_('Name'), max_length=100, blank=False, unique=True)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)

    def __str__(self) -> str:
        return self.name
