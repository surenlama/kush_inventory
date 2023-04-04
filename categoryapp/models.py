from django.db import models
from inventory.utils import ACTIVE_CHOICES

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=15)
    code = models.CharField(max_length=4)
    status = models.CharField(max_length=250,choices=ACTIVE_CHOICES,default="no_active")


class Category(models.Model):
    name = models.CharField(max_length=15)
    code = models.CharField(max_length=4)
    status = models.CharField(max_length=250,choices=ACTIVE_CHOICES,default="no_active")

