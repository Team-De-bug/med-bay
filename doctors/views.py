from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required()
def appointment(request):
    user = User.objects.filter(username=request.user)[0]
    if user.staff.role != "d":
        return HttpResponseForbidden(HttpResponse("<h1>Only for doctors</h1>"))

    cases = user.staff.doctor.cases_set.filter(status="t")

    print(cases)
    return render(request, 'doctors/appointments.html', context={"cases": cases})
