from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pharma.models import Prescription
from .forms import CaseProcessing


# Create your views here.
@login_required()
def appointment(request):
    user = User.objects.filter(username=request.user)[0]
    if user.staff.role != "d":
        raise PermissionDenied

    if request.method == "POST":
        form_data = CaseProcessing(request.POST)
        if form_data.is_valid():
            print("valid input")
            print(form_data.cleaned_data['has_pres'])
        return redirect("red")
    else:
        cases = user.staff.doctor.cases_set.filter(status="t")
        form = CaseProcessing()
        print(cases)
        return render(request, 'doctors/appointments.html', context={"cases": cases, 'form': form})
