from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from ..forms import UserLoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.name}')
                return redirect('home')
            else:
                messages.error(request, 'Incorrect email or password')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = UserLoginForm()

    return render(request, 'users_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out')
    return redirect('home')

def test_authentication(request):
    email = "your_email@example.com"
    password = "your_password"
    user = authenticate(email=email, password=password)
    
    if user is not None:
        return HttpResponse(f"User authenticated: {user}")
    else:
        return HttpResponse("Authentication failed")
