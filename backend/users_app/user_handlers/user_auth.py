from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import path
from ..forms import UserLoginForm

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, f'Welcome', {user.first_name})
                    return redirect('home')
                else:
                    messages.error(request, 'Incorrect password')
            except User.DoesNotExist:
                messages.error(request, 'User not found')
            else:
                form = UserLoginForm()
            return render(request, 'users_app/login.html', {'form': form})
        
    
@login_required

def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out')
    return redirect('home')