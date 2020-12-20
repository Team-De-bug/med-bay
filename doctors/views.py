from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required()
def appointment(request):
    user = User.objects.filter(username=request.user)[0]
    if user.staff.role != "d":
        raise PermissionDenied

    cases = user.staff.doctor.cases_set.filter(status="t")

    print(cases)
    return render(request, 'doctors/appointments.html', context={"cases": cases})
