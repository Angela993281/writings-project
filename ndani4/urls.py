from django.urls import path
from. import views

# app_name = 'ndani4' 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payment/', views.payment, name='payment'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('submit/', views.submit, name='submit'),
]
  

