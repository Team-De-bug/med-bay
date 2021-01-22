from django.contrib.auth.decorators import login_required
from pharma.models import Prescription, Stock, Medicine
from django.shortcuts import render, redirect
from patients.models import Cases, Patient
from admins.utils import validate_access
from django.http import HttpResponse
from .forms import CaseProcessing
from datetime import date
import json


# Create your views here.
@login_required()
def appointment(request):

    # Getting the user from the request
    user = validate_access(request, 'd')

    # Getting the list of patients who are to be attended
    d = date.today()
    cases = user.staff.doctor.cases_set.filter(status="t", appointed_date__date=d)

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
                    response = redirect('doctor:add_prescription')
                    response['Location'] += f'?id={case.id}'
                    return response

            # Redirecting user back to appointments page
            return redirect("doctor:dashboard")

    # If not then just loading the page
    else:
        form = CaseProcessing()
        print(cases)
        return render(request, 'doctors/appointments.html', context={"cases": cases, 'form': form})
    
    
@login_required()
def case_archive(request):
    
    user = validate_access(request, 'd')

    # Getting the cases under the doctor
    cases = user.staff.doctor.cases_set.filter(status='d')
    patients = {}

    # Adding patients as the keys and the done cases as values
    for case in cases:
        if case.patient not in patients:
            patients[case.patient] = case.patient.cases_set.filter(status='d')

    return render(request, 'doctors/case_archive.html', context={'patients': patients})


# Recover prescriptions in case of issues
@login_required()
def prescription(request):
    
    # Getting the user from the request
    user = validate_access(request, 'd')

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
    validate_access(request, 'd')

    # Getting the case from case id
    case = Cases.objects.get(id=int(request.GET["id"]))

    # Rendering the html file
    return render(request, 'doctors/add-prescription.html', context={"case": case})


# List available medicines
@login_required()
def list_medicines(request):

    all_medicines = []
    for medicine in Stock.objects.filter(deleted=False):
        if medicine.quantity > 0: all_medicines.append(medicine)

    medicines = {}
    for stock in all_medicines:
        medicines[stock.id] = stock.name
    return HttpResponse(json.dumps(medicines), content_type="application/json")


# Saving the prescription
@login_required()
def save_prescription(request):

    # Getting the user from the request
    validate_access(request, 'd')

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


# View patient history
@login_required()
def view_history(request):
    validate_access(request, 'd')

    # Getting the cases from the request object
    p_id = int(request.GET['id'])
    patient = Patient.objects.get(id=p_id)
    cases = patient.cases_set.all()
    print(cases)

    return render(request, 'doctors/case-history.html', context={'cases': cases})
