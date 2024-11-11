from .models import Company
from django.forms import ModelForm, TextInput

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fileds = ['name', 'llc-number', 'email', 'password']
		exclude = ['id']

		widgets = {
			"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Your company name'
			}),
			"LLC_Number": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Your company LLC'
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