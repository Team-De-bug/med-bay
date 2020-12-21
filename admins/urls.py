from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(template_name="admins/login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="admins/logout.html"), name="logout"),
    path("confirm", views.confirm_logout, name='confirm-logout'),
    path("", views.home, name="home"),
    path("redirect", views.redirect_login, name="red")
]
