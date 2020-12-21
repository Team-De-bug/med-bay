from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock


# Create your views here.
@login_required
def shop(request):
    user = User.objects.filter(username=request.user).first()
    if user.staff.role != "p":
        raise PermissionDenied()
    else:
        items = Stock.objects.all()
        return render(request, "pharma/shop.html", context={'items': items})
