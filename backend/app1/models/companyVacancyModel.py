from django.db import models
from enum import Enum
from .companyModel import Company

class StatusEnum(Enum):
    active = 0
    hired = 1
    canceled = 2

class CompanyVacancy(models.Model) :

	vacancy_id = models.AutoField(primary_key=True)
	name =  models.CharField(max_length=150, blank=False)
	# company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
	company_id = models.IntegerField()
	# hired_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

	STATUS_CHOICES = [
		(0, 'intership'),
		(1, 'part-time job'),
		(2, 'full-time job') ]
	employment = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
	location = models.IntegerField()
	salary = models.CharField(max_length=10) # если приходит +2000, то это значит от 2000, если приходит -2000, значит до 2000. Просто 2000 - просто 2000, если пришла пустая строка, то без указанной зарплаты)
	skills = models.CharField(max_length=1000) #  string (one by one separated by space)
	experience = models.IntegerField() # ожидаемый стаж работы (в годах), 0 - без опыта работы
	comment = models.CharField(max_length=1000)
	is_degree_required = models.BooleanField()
	status = models.PositiveSmallIntegerField(choices=[(status.value, status.name) for status in StatusEnum],
        default=StatusEnum.active.value)