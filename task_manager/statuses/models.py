from django.db import models


# Create your models here.
class TaskStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now=True)
