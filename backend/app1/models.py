from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

# Create your models here. Related to databases. 
# In other worlds, model is a table

# migration = writing changes of the model

class Company(models.Model) :
	name = models.CharField(max_length=30, blank=False)
	password = models.CharField(max_length=128, blank=False, default='',
		validators=[RegexValidator(
			regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',  # At least one letter and one number, minimum 8 chars
			message="Password must contain at least one letter, one number, and be at least 8 characters."
		)]
	)
	# email = models.EmailField(unique=True, null=True, blank=True)
	email = models.EmailField(unique=True, default='', blank=False)
	#should be unique=True
	LLC_Number = models.CharField(max_length=55, default='', blank=False)
	id = models.AutoField(primary_key=True)

	def set_password(self, raw_password):
		self.password = make_password(raw_password)
	
	def __str__(self):
		return self.name