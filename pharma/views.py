from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock

# Create your views here.
def shop(request):
    items = Stock.objects.all()[0]
    return render(request, "pharma/shop.html", context={'items':items})
   
