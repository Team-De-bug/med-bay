from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AuthForm


# Edit the function below.
def home(request):
    return render(request, "admins/home.html")


# login page
class LoginView(auth_views.LoginView):
    form_class = AuthForm


# Confirm Logout page
def confirm_logout(request):
    return render(request, "admins/confirm_logout.html")

# login redirect
@login_required()
def redirect_login(request):
    user = User.objects.filter(username=request.user)[0]
    if user.staff.role == "d":
        return redirect('appointments')
    if user.staff.role == "a":
        return redirect('home')
    if user.staff.role == "p":
        return redirect('shop')
    else:
        raise Http404("page not found")
