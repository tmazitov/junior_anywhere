from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    email = models.EmailField(blank=False)
    phone = PhoneNumberField(blank = False)
    password = models.CharField(max_length=20, blank=False)

class UserApply(models.Model):
    pass
class UserResume(models.Model):
    pass