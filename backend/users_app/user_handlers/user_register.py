from django.shortcuts import render, redirect
from users_app.models import User
from django.contrib import messages
from ..forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import path

def index_page(request):
    all_users = User.objects.all()
    return render(request, 'home.html', {'data': all_users})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(request, f'Welcome to SunflowerJunior {username}')
            return redirect('blog:home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

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