"""oshowa1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from USers import views as User_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from ndani4 import views as ndani_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ndani4.urls')),
    path('dashboard/', ndani_views.dashboard, name='dashboard'),  # FIXED: Directly linking dashboard
    path('register/', User_views.register, name='register'),
    path('login/', User_views.user_login, name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='USers/logout.html'), name='logout'),
    path('payment/', include('ndani4.urls')),
    path('withdraw/', include('ndani4.urls')),
    path('submit/', include('ndani4.urls')),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
