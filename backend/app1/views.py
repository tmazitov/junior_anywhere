from django.shortcuts import redirect, render

from app1.models import Company
from .forms import CompanyForm

# Create your views here. Connect models and templates 

def index_page(request):
	# get all records from the model OR all objects of this model
	all_companies = Company.objects.all()
	return render(request, 'index.html')

def create(request):
	error = ''
	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create')  # Redirect to the same page after saving
		else:
			error = 'invalid form'
	form = CompanyForm()
	data = {
		'form': form,
		'error' : error
	}

	return render(request, 'index.html', data)