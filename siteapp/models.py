from django.db import models
from inventory.utils import ACTIVE_CHOICES

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=4)
    site_incharge = models.CharField(max_length=250)
    contact_details = models.TextField()


