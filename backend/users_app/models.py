from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=20, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    def __str__(self):
        return f'{self.second_name} {self.name}'


class UserApply(models.Model):
    pass
class UserResume(models.Model):
    pass