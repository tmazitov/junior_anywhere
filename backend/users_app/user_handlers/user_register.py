from django.shortcuts import render
from users_app.models import User
from ..forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt

#Returns all users list as a JSON
def index_page(request):
    if request.method == 'GET':
        all_users = User.objects.all().values('id', 'name', 'email', 'phone_number')
        return JsonResponse({'users': list(all_users)}, safe=False, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

#when register a new user will return JSON
def register(request):
    if request.method == 'POST':
        try:
            data = json = json.loads(request.body)
            form = UserRegisterForm(data)
            if form.is_valid():
                user = form.save()
                return JsonResponse({'message': f'Welcome to SunflowerJunior {user.name}', 'user_id': user.id}),
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
#returns profile of a user
def profile(request):
    if request.method == 'GET':
        user = request.user
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,        
        }
        return JsonResponse(user_data, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


    # NEW USER
    # new_user = User(name='new', second_name='user', email='newuser@gmail.com', password='1234', phone_number='+971540000000')
    # new_user.save()

    # UPDATE USER
    # user_to_change = User.objects.get(userId=5)
    # user_to_change.second_name = 'NEW'
    # user_to_change.save()


    # DELETE USER 
    # User.objects.get(userId=4).delete()


    # FILTER WITH PROPERTY
    # users_filtered = User.objects.filter(name='asya')
    # print(users_filtered)

    # WRITE ALL USERS IN TERMINAL
    # for i in all_users:
    #     print(f'Second name: {i.second_name}, ID: {i.userId}')

    # my_dictionary = {'data': 'Привет!', 'data2': ' всем привет'}
    # all_users = User.objects.all()
    # return render (request, 'index.html', {'data': all_users}) 