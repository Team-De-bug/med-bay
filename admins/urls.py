from django.urls import path
from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(template_name="admins/login.html"), name="login"),
    path("", views.home, name="home"),
    path("redirect", views.redirect_login, name="red")
]
