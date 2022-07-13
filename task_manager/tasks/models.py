from django.db import models
from django.conf import settings
from task_manager.statuses.models import TaskStatus
from django.utils.translation import gettext as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(_('Name'), max_length=100, blank=False, unique=True)
    description = models.TextField(_('Description'))
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='created')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='assigned')
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)
    date_modified = models.DateTimeField(_('Date Modified'), auto_now=True)
