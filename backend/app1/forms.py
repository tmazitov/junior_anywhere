from .models import Company
from django.forms import ModelForm, TextInput

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fileds = ['name', 'email', 'password']
		exclude = ['companyID']

		widgets = {
			"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Your company name'
			}),
			"email": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'example@mail.com'
			}),
			"password": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'password1234'
			}),
		}