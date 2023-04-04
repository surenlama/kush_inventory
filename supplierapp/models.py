from django.db import models
from officeapp.models import Office
from inventory.utils import ACTIVE_CHOICES

# Create your models here.
class Supplier(models.Model):
    office = models.ForeignKey(Office,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    details = models.TextField()
    previous_balance = models.IntegerField()
    status = models.CharField(max_length=250,choices=ACTIVE_CHOICES,default="no_active")

