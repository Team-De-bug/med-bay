from django.contrib.auth.decorators import login_required
from admins.utils import validate_access
from django.shortcuts import render
from .models import Entries


# Create your views here.
@login_required()
def home(request):
    validate_access(request, 'ac')
    return render(request, 'accounts/home.html')


@login_required()
def entries(request):
    validate_access(request, 'ac')
    entries = Entries.objects.all()
    return render(request, 'accounts/entries.html', context={"entries": entries})
