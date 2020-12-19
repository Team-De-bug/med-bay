from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(template_name="admins/login.html"), name="login"),
    path("", views.home, name="home"),
]
