from django.contrib.auth.decorators import login_required
from admins.utils import validate_access
from django.shortcuts import render


# Create your views here.
@login_required()
def home(request):
    validate_access(request, 'ac')
    return render(request, 'accounts/home.html')
