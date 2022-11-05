from django.db import models
from datetime import datetime, date
# Create your models here.


class DonorRegister(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dob = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    lastdonatedate = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.fname
