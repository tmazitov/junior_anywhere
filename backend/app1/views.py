from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password

from app1.models import Company
from .forms import CompanyForm
from django.http import JsonResponse


# Connect models and templates 

def auth(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    company = Company.objects.filter(email=email).first()

    if company and check_password(password, company.password):
        return JsonResponse({'id': company.id, 'name': company.name})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
        data = {
            'name': company.name,
            'llc_number': company.llc_number,
            'id': company.id,
        }
        return JsonResponse(data)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)

from django.shortcuts import render, redirect
from .forms import CompanyForm

# def index_page(request):
# 	# get all records from the model OR all objects of this model
# 	all_companies = Company.objects.all()
# 	form = CompanyForm()
# 	return render(request, 'company/login.html', {'form': form})


def index_page(request):
    # Получаем все записи из модели
    all_companies = Company.objects.all()
    form = CompanyForm()

    # Проверка, если форма отправлена методом POST
    if request.method == 'POST':
        print("Form submitted")  # Проверяем, что форма отправлена
        action = request.POST.get('action')  # Получаем значение кнопки (login или register)
        print(f"Action: {action}")  # Проверяем, какое действие было выбрано

        if action == 'log in':
            response_data = {
                'status': 'login',
                'message': 'Login button pressed'
            }
            print("Login button pressed")
            return render(request, 'company/login.html', {'form': form})
        
        elif action == 'sign up':
            print("Register button pressed")
            return render(request, 'company/register.html', {'form': form})
    
    # Если запрос не POST, просто рендерим страницу login по умолчанию
    return render(request, 'company/login.html', {'form': form}) 



def register_success(request):
    return render(request, 'company/register_success.html')

# def render_register(request):
# 	return render(request, 'company/register.html') 

def register(request):
    # Обработка POST-запроса
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        
        # Проверка, существует ли компания с таким email
        email = request.POST.get('email')
        if Company.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already in use'}, status=400)
        
        # Если форма валидна
        if form.is_valid():
            company = form.save(commit=False)
            company.set_password(form.cleaned_data['password'])  # Хешируем пароль
            company.save()
            return JsonResponse({'id': company.id, 'name': company.name, 'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    
    # Обработка GET-запроса, если нужно вернуть пустую форму
    form = CompanyForm()
    form_data = {field.name: field.value() for field in form}  # Пример структуры формы
    return JsonResponse({'form': form_data})


# def register(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     llc_number = request.POST.get('llc_number')

#     if Company.objects.filter(email=email).exists():
#         return JsonResponse({'error': 'Email already in use'}, status=400)

#     company = Company(name=name, email=email, llc_number=llc_number)
#     company.set_password(password)  # Сохранение с хешированием
#     company.save()

#     return JsonResponse({'id': company.id, 'name': company.name})
# retun .json, not index.html