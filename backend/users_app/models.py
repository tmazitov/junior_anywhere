from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank = False)
    salary = models.IntegerField(blank=True)
