from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login  # Rename to avoid conflict




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm  # Import the new form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save user but don't commit yet
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()  # Now save user
            auth_login(request, user)  # Automatically log them in
            messages.success(request, f'{user.username}, your account has been created!')
            return redirect('dashboard')  
        else:
            print(form.errors)  # Debugging
            messages.error(request, 'There was an error during registration. Please try again.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'USers/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')  # FIXED: Namespace included
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'USers/login.html', {'form': form})

    
    







