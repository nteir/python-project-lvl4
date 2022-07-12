from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class TaskStatus(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    date_created = models.DateTimeField(_('Date Created'), auto_now=True)
