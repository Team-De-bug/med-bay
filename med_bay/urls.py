"""med_bay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from admins.views import LoginView, confirm_logout, home, redirect_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('admins.urls')),
    path('doctor/', include('doctors.urls')),
    path('pharmacy/', include('pharma.urls')),
    path("login", LoginView.as_view(template_name="admins/login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="admins/logout.html"), name="logout"),
    path("confirm", confirm_logout, name='confirm-logout'),
    path("", home, name="home"),
    path("redirect", redirect_login, name="red")
]


handler404 = 'med_bay.error_views.error_404_handler'
handler403 = 'med_bay.error_views.error_403_handler'
