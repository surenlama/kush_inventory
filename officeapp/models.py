from django.db import models

# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email_address = models.CharField(max_length=250)
