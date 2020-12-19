from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import AuthForm


# Edit the function below.
def home(request):
    return render(request, "admins/home.html")


# login page
class LoginView(auth_views.LoginView):
    form_class = AuthForm
