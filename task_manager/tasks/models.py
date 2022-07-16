from django.db import models
from django.conf import settings
from task_manager.statuses.models import TaskStatus
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, verbose_name=_('Status'))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='created',
        verbose_name=_('Author')
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='assigned',
        verbose_name=_('Executor')
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date Modified'))
    labels = models.ManyToManyField(
        Label,
        through='TaskLabelRelation',
        blank=True,
        verbose_name=_('Labels')
    )


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
