from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict

from app1.models import CompanyVacancy
from app1.models import Company
from app1.forms.companyVacancyForm import CompanyVacancyForm
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json

#search for a particular company in database by company_id and return data
#if this company's vacancy by vacancy_id
@require_http_methods(["GET"])
def get_company_vacancy_data(request, company_id, vacancy_id):
	try:
		companyVacancy = CompanyVacancy.objects.get(vacancy_id=vacancy_id)
		data = model_to_dict(companyVacancy)
		return JsonResponse({'status': 'success', 'data': data}, status=200)
	except CompanyVacancy.DoesNotExist:
		return JsonResponse({'error': 'CompanyVacancy not found'}, status=404)

@require_http_methods(["GET", "POST"])
def registerVacancy(request, company_id):
	if request.method == 'POST':
		# Попробуем сначала получить JSON данные из тела запроса
		try:
			data = json.loads(request.body)  # Парсим JSON данные из тела запроса
			# Include company_id in the form data
			data['company_id'] = company_id  # Assign company_id to the company field
			print("JSON data:", data)
		except json.JSONDecodeError:
			data = request.POST  # Если это не JSON, используем request.POST
			print("Form data:", data)
				
		form = CompanyVacancyForm(data)  # Передаем данные в форму
		if form.is_valid():
			vacancy = form.save(commit=False)
			vacancy.company_id = company_id
			vacancy.save()
			return JsonResponse({'vacancy_id': vacancy.vacancy_id}, status=200)
		else:
			return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

	# Обработка GET-запроса, если нужно вернуть пустую форму
	form = CompanyVacancyForm()
	form_data = {field.name: field.value() for field in form}  # Пример структуры формы
	return JsonResponse({'form': form_data})

@require_http_methods(["DELETE"])
def cancel_vacancy(request, company_id, vacancy_id):
    try:
        # Query the vacancy directly using company_id and vacancy_id for efficiency
        vacancy = CompanyVacancy.objects.get(pk=vacancy_id, company_id=company_id)
        
        if vacancy.status == 0:
            vacancy.status = 2  # Set to canceled
            vacancy.save()  # Commit the change
            return JsonResponse({'status': 'success', 'message': 'Vacancy canceled successfully.'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'message': 'Vacancy is not active.'}, status=400)
    except CompanyVacancy.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'No vacancy found with the provided ID for this company.'}, status=404)

@require_http_methods(["PATCH"])
def hire(request, company_id, vacancy_id, hired_user_id):
	try:
		vacancy = CompanyVacancy.objects.get(pk=vacancy_id, company_id=company_id)
				
		if vacancy.status == 0 & vacancy.hired_user_id == 0:
			vacancy.status = 1
			vacancy.hired_user_id = hired_user_id
			vacancy.save()  # Commit the change
			return JsonResponse({'status': 'success', 'message': 'User has been hired for vacancy successfully.'}, status=201)
		else:
			return JsonResponse({'status': 'error', 'message': 'Vacancy is not active.'}, status=400)
	except CompanyVacancy.DoesNotExist:
		return JsonResponse({'status': 'error', 'message': 'No vacancy found with the provided ID for this company.'}, status=404)