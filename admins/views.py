from .forms import AuthForm, PatientForm, CaseCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .utils import validate_access
from .models import Staff
import json


# Edit the function below.
def home(request):
    return render(request, "admins/home.html")


# staff attendance
@login_required()
def attendance(request):

    # Checking if the user is an Admin member
    validate_access(request, 'a')

    # Getting the list of doctors
    doctors = Staff.objects.filter(role='d')

    # Checking if update is available
    if "update" in request.GET:

        # Getting the attendance from the request
        data = json.loads(request.GET["attendance"])

        # Updating the doctor attendance
        for doc in data:
            doctor = doctors.get(id=int(doc)).doctor
            doctor.availability = data[doc]
            doctor.save()

        # Returning the success message
        return HttpResponse("Success!")

    return render(request, "admins/attendance.html", context={'doctors': doctors})


# Patient Creation Page
@login_required()
def create_patient(request):
    validate_access(request, 'a')

    # if form data provided
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = PatientForm()
    return render(request, "admins/create_patient.html", context={'form': form})


# Create case
def create_case(request):
    form = CaseCreationForm()
    form.set_choices()
    return render(request, "admins/create_case.html", context={'form': form})


""" <===========================|******| Base Routes |******|===========================> """


# login page
class LoginView(auth_views.LoginView):
    form_class = AuthForm


# Confirm Logout page
def confirm_logout(request):
    return render(request, "admins/confirm_logout.html")


# login redirect
@login_required()
def redirect_login(request):
    user = User.objects.get(username=request.user)
    if user.staff.role == "d":
        return redirect('doctor:dashboard')
    if user.staff.role == "a":
        return redirect('home')
    if user.staff.role == "p":
        return redirect('pharma:shop')
    else:
        raise Http404("page not found")
