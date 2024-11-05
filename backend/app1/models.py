from django.db import models

# Create your models here. Related to databases. 
# In other worlds, model is a table

# migration = writing changes of the model
class Company(models.Model) :
	name = models.CharField(max_length=20, blank=False)
	# companyID mixed chars and integers = models.IntegerField(default=0)
	# email
	# password mixed chars and integers
	def __str__(self):
		return self.name 