from django.shortcuts import render

from backend.app1.models import Company

# Create your views here. Connect models and templates 

def index_page(request):
	# get all records from the model
	all_companies = Company.objects.all()
	return render(request, 'index.html')
