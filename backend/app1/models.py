from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

# Create your models here. Related to databases. 
# In other worlds, model is a table

# migration = writing changes of the model

class Company(models.Model) :
	name = models.CharField(max_length=30, blank=False)
	password = models.CharField(max_length=128, blank=False, default='')
	email = models.EmailField(unique=True, default='', blank=False)
	LLC_Number = models.CharField(max_length=55, unique=True, default='', blank=False)
	id = models.AutoField(primary_key=True)

	def set_password(self, raw_password):
		self.password = make_password(raw_password)
	
	def __str__(self):
		return self.name
	

from enum import Enum

class StatusEnum(Enum):
    active = 0
    hired = 1
    canceled = 2

class CompanyVacancy(models.Model) :

	id = models.AutoField(primary_key=True)
	name =  models.CharField(max_length=150, blank=False)
	#company_id: number - id компании, сделать связь между ними
	# hired_user_id: number - id нанятого пользователя (без связи так как пользователей делает Лера)
	STATUS_CHOICES = [
		(0, 'intership'),
		(1, 'part-time job'),
		(2, 'full-time job') ]
	employment = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
	location = models.IntegerField()
	salary = models.CharField() # если приходит +2000, то это значит от 2000, если приходит -2000, значит до 2000. Просто 2000 - просто 2000, если пришла пустая строка, то без указанной зарплаты)
	skills = models.CharField() #  string (one by one separated by space)
	experience = models.IntegerField() # ожидаемый стаж работы (в годах), 0 - без опыта работы
	comment = models.CharField(max_length=1000)
	is_degree_required = models.BooleanField()
	status = models.PositiveSmallIntegerField(choices=[(status.value, status.name) for status in StatusEnum],
        default=StatusEnum.OPTION_0.value)