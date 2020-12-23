from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from pharma.models import Prescription, Stock
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import CaseProcessing
from patients.models import Cases
import json


# Create your views here.
@login_required()
def appointment(request):

    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied

    # Getting the list of patients who are to be attended
    cases = user.staff.doctor.cases_set.filter(status="t")

    # Checking if a patient diagnosis is being sent
    if request.method == "POST":
        form_data = CaseProcessing(request.POST)
        if form_data.is_valid():
            case_id = form_data.cleaned_data['id']

            # Making sure the form is not tamperd with and the case belongs to the doctor
            case = None
            for c in cases:
                if c.id == case_id:
                    case = c

            # if the case belongs to the doctor and is to be handled
            if case:

                # Saving the case data and updating the case state
                case.desc = form_data.cleaned_data['desc']
                case.status = 'd'
                case.save()

                # If the case has a prescription then making one
                if form_data.cleaned_data["has_pres"]:
                    pres = Prescription(case=case)
                    pres.save()

                    # Redirecting user to prescription page
                    response = redirect('add-prescription')
                    response['Location'] += f'?id={case.id}'
                    return response

            # Redirecting user back to appointments page
            return redirect("appointments")

    # If not then just loading the page
    else:
        form = CaseProcessing()
        print(cases)
        return render(request, 'doctors/appointments.html', context={"cases": cases, 'form': form})
    
    
@login_required()
def prescriptions(request):
    
    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied
    return render(request, 'doctors/prescriptions.html')


@login_required()
def prescription(request):
    
    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied
        
    return render(request, 'doctors/prescription.html')


@login_required()
def add_prescription(request):
    
    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied

    # Getting the case from case id
    case = Cases.objects.get(id=int(request.GET["id"]))

    # Rendering the html file
    return render(request, 'doctors/add-prescription.html', context={"case": case})


# List available medicines
@login_required()
def list_medicines(request):
    stocks = Stock.objects.all()
    medicines = {}
    for stock in stocks:
        medicines[stock.id] = stock.name
    return HttpResponse(json.dumps(medicines), content_type="application/json")


# Saving the prescription
def save_prescription(request):

    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied