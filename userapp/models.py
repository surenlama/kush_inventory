from django.db import models
from inventory.utils import ACTIVE_CHOICES
# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=250)

class User(models.Model):
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email_address = models.CharField(max_length=250)
    status = models.CharField(max_length=250,choices=ACTIVE_CHOICES,default="no_active")
