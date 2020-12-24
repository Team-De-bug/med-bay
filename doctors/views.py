from django.contrib.auth.decorators import login_required
from pharma.models import Prescription, Stock, Medicine
from django.core.exceptions import PermissionDenied
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
def case_archive(request):
    
    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied

    # Getting the cases under the doctor
    cases = user.staff.doctor.cases_set.filter(status='d')
    patients = {}

    # Adding patients as the keys and the done cases as values
    for case in cases:
        if case.patient not in patients:
            patients[case.patient] = case.patient.cases_set.filter(status='d')

    print(patients)
    return render(request, 'doctors/case_archive.html', context={'patients': patients})


# Recover prescriptions in case of issues
@login_required()
def prescription(request):
    
    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied

    # Getting the list of cases
    cases = Cases.objects.filter(doctor=user.staff.doctor)
    prescriptions = []

    for case in cases:
        # checking if prescription exists and the state is created
        if hasattr(case, 'prescription'):
            if case.prescription.status == 'c':
                prescriptions.append(case.prescription)

    return render(request, 'doctors/prescription.html', context={"prescriptions": prescriptions})


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
@login_required()
def save_prescription(request):

    # Getting the user from the request
    user = User.objects.filter(username=request.user)[0]

    # Making sure if the user is a doctor
    if user.staff.role != "d":
        raise PermissionDenied

    # Getting the medicines and the related case
    case = Cases.objects.get(id=int(request.GET['case_id']))
    medicines = json.loads(request.GET["medicines"])

    # Printing the value for debubbing purposes
    print(case, medicines)

    # Making the medicine instances and relating to case
    for med in medicines:
        item = Stock.objects.get(id=int(med))
        medicine = Medicine(prescription=case.prescription, item=item, quantity=int(medicines[med]))
        medicine.save()

    # Updating prescription state
    case.prescription.status = 'p'
    case.prescription.save()

    # returning success message
    return HttpResponse("success")
