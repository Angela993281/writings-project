from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

def home(request):
    return render(request, 'ndani4/home.html')

@login_required(login_url='login')  # Redirects to login page if not authenticated
def dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'ndani4/dashboard.html', {'tasks': tasks})

@login_required(login_url='login') 
def payment(request):
    return render(request, 'ndani4/payment.html')

@login_required(login_url='login') 
def withdraw (request):
    return render(request, 'ndani4/withdraw.html')

@login_required(login_url='login') 
def submit (request):
    return render(request, 'ndani4/submit.html')

