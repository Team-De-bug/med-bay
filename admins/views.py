from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import AuthForm


# Edit the function below.
def home(request):
    return render(request, "admins/home.html")


# login page
class LoginView(auth_views.LoginView):
    form_class = AuthForm


@login_required()
# login redirect
def redirect_login(request):
    user = User.objects.filter(username=request.user)[0]
    if user.staff.role == "d":
        return redirect('appointments')
    if user.staff.role == "a":
        return redirect('home')
    else:
        return Http404()
