from django.db import models
from django.core.validators import RegexValidator

# Create your models here. Related to databases. 
# In other worlds, model is a table

# migration = writing changes of the model

class Company(models.Model) :
	name = models.CharField(max_length=30, blank=False)
	companyID = models.IntegerField(default=0)
	password = models.CharField(max_length=128, blank=False, default='TempPass1234',
		validators=[RegexValidator(
			regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',  # At least one letter and one number, minimum 8 chars
			message="Password must contain at least one letter, one number, and be at least 8 characters."
		)]
	)
	# email = models.EmailField(unique=True, null=True, blank=True)
	email = models.EmailField(unique=True, default='default@example.com', blank=False)

	def __str__(self):
		return self.name