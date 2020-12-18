from django.shortcuts import render
from django.http import HttpResponse


# Edit the function below.
def home(request):
    return render(request, "admins/home.html")
