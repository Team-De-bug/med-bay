from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from admins.utils import validate_access
from .forms import StockForm, BillForm
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from . import utils
import json


# Create your views here.
@login_required()
def shop(request):

    # Checking if user is allowed visit the site
    validate_access(request, 'p')

    # Getting the list of stocks
    items = Stock.objects.filter(deleted=False)
    items = list(items)
    for item in items:

        # Removing out of stock items
        if item.quantity < 1:
            items.remove(item)

    print(render(request, "pharma/shop.html", context={'items': items}).content)
    return render(request, "pharma/shop.html", context={'items': items})


# Placing order when order button is pressed
@login_required()
def place(request):

    user = validate_access(request, 'p')
    ID = request.GET['product_id']
    qty = int(request.GET['product_amount'])
    item = Stock.objects.filter(id=ID)[0]
    orders = user.staff.order_set.all()

    # Checking if item already in cart
    in_cart = False
    for order in orders:
        if order.item.id == item.id:
            in_cart = True

    # If the item is already in cart
    if in_cart:
        order = user.staff.order_set.filter(item__id=item.id)[0]
        order.quantity += qty

    # Creating a new order if not already there
    else:
        order = Order(user=user.staff, item=item, quantity=qty)

    # Updating the item stock and saving changes
    item.quantity -= qty
    order.save()
    item.save()

    return HttpResponse("success")


@login_required()
def remove(request):

    user = validate_access(request, 'p')

    # Getting the item id and quantity to reduce from request
    ID = int(request.GET['product_id'])
    reduce = int(request.GET['remove_amount'])

    # Getting the respective items and objects from the table
    item = Stock.objects.filter(id=ID)[0]
    order = user.staff.order_set.filter(item__id=item.id)[0]

    # Checking if the quantity in order will be 0
    if order.quantity == reduce:
        order.delete()
    else:
        order.quantity -= reduce
        order.save()

    # Updating item quantity and saving changes
    item.quantity += reduce
    item.save()

    return render(request, "pharma/cart.html", {'cart': cart})


@login_required()
def add_one(request):

    user = validate_access(request, "p")

    # Getting the product id from the request
    ID = int(request.GET['product_id'])

    # Getting the respective items and orders
    item = Stock.objects.get(id=ID)
    order = user.staff.order_set.get(item__id=item.id)

    # Changing the quantity accordingly
    order.quantity += 1
    item.quantity -= 1

    # Saving the changes
    order.save()
    item.save()

    return render(request, "pharma/cart.html", {'cart': cart})


@login_required()
def cart(request):

    user = validate_access(request, 'p')

    orders = user.staff.order_set.all()
    total = utils.get_total(orders)

    return render(request, "pharma/cart.html", {'cart': orders, 'total': total})


# Getting the name and phone number for bill
@login_required()
def bill_info(request):

    # Getting the orders
    user = validate_access(request, 'p')
    orders = user.staff.order_set.all()
    print(orders)
    print(request.GET)

    # Redirecting back to home if there are no orders
    if not orders:
        return redirect("pharma:shop")

    # Checking if the form data is recieved
    if request.method == "POST":
        form = BillForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            # Redirecting user to prescription page
            response = redirect('pharma:bill')
            response['Location'] += f'?name={name}&phone={phone}'
            return response

    else:
        form = BillForm()

    return render(request, "pharma/bill_info.html", context={'form': form})


# showing the bill after purchase
@login_required()
def bill(request):
    
    # Getting the orders
    user = validate_access(request, 'p')
    orders = user.staff.order_set.all()
    print(orders)
    print(request.GET)

    # Redirecting back to home if there are no orders
    if not orders:
        return redirect("pharma:shop")

    # Generating the bill objects
    bill = utils.generate_bill(name=request.GET["name"], contact_num=request.GET["phone"],
                               date=timezone.now(), orders=orders)

    # Clearing the cart
    for order in orders:
        order.delete()

    # getting all the bill units to send in context
    bill_units = bill.billunit_set.all()
    print(bill_units, bill)
    total = utils.get_bill_total(bill_units)

    return render(request, 'pharma/bill.html', context={'bill': bill, 'bill_unit': bill_units, 'total': total})


@login_required()
def add_stock(request):
    validate_access(request, 'p')
    if request.method == "POST":
        form = StockForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']

            stock = Stock.objects.create(name=name, desc="med", price=price, quantity=quantity)
            stock.save()

            return redirect("pharma:shop")

    return render(request, 'pharma/add_stock.html')


@login_required()
def remove_stock(request):

    # making sure the user is a pharmacist
    validate_access(request, "p")

    # Deleting the product if product_id is sent
    if 'product_id' in request.GET:
        print(f"deleting {request.GET['product_id']}")
        id = int(request.GET['product_id'])
        item = Stock.objects.get(id=id)
        item.deleted = True
        item.save()

    # loading the list of stocks
    items = Stock.objects.filter(deleted=False)

    return render(request, 'pharma/remove_stock.html', context={'items': items})


# Bill archive
@login_required()
def bill_archive(request):
    validate_access(request, 'p')
    bills = Bill.objects.all()
    return render(request, 'pharma/bill_archive.html', context={"bills": bills})


# Bill archive viewer
def bill_archive_viewer(request):

    bill = Bill.objects.get(id=int(request.GET['id']))
    bill_units = bill.billunit_set.all()
    total = utils.get_bill_total(bill_units)

    return render(request, 'pharma/bill.html', context={'bill': bill, 'bill_unit': bill_units, 'total': total})


@login_required()
def order_prescription(request):
    validate_access(request, 'p')
    prescriptions = Prescription.objects.filter(status='p')

    # placing order if request has id
    if 'id' in request.GET:
        pres = prescriptions.get(id=int(request.GET['id']))

        # returning a redirect if medicine is not available
        issue_stock = {}
        for med in pres.medicine_set.all():
            if med.quantity > med.item.quantity or med.item.deleted:
                issue_stock[med.item.id] = med.item.name

        # if There are missing stock or out of stock medicines
        if issue_stock:
            return HttpResponse(json.dumps(issue_stock), content_type='application/json', status=418)

        # Generating the bill if the objects are in stock
        bill = utils.generate_bill(name=pres.case.patient.name, contact_num=pres.case.patient.phone,
                                   date=timezone.now(), orders=pres.medicine_set.all())

        # Updating the prescription status and saving changes
        pres.bill = bill
        pres.status = 'd'
        pres.save()

        # giving a redirect to view the bill
        return HttpResponse(json.dumps({'id': bill.id}), content_type='application/json')

    return render(request, 'pharma/orders.html', context={'prescriptions': prescriptions})


@login_required()
def edit_prescription(request):
    user = validate_access(request, 'p')

    pres = Prescription.objects.get(id=int(request.GET["id"]))

    # if the list was edited
    if 'save' in request.GET:
        medicine_ids = json.loads(request.GET['medicines'])
        items = Stock.objects.filter(deleted=False)
        epres = EditedPrescription(user=user.staff, pres=pres)
        epres.save()

        for med_id in medicine_ids:
            item = items.get(id=med_id)
            med = EPMedicine(prescription=epres, item=item, quantity=int(medicine_ids[med_id]))
            med.save()
            print(med, 'saved')

        bill = utils.generate_bill(name=pres.case.patient.name, contact_num=pres.case.patient.phone,
                                   date=timezone.now(), orders=epres.medicines.all())

        for med in epres.medicines.all():
            print(med)

        pres.bill = bill
        pres.status = 'd'
        pres.save()

        return HttpResponse(json.dumps({'bill_id': bill.id}), content_type='application/json')

    # getting valid medicines from stock
    all_medicines = []
    for medicine in Stock.objects.filter(deleted=False):
        if medicine.quantity > 0: all_medicines.append(medicine)

    medicines = json.loads(request.GET['medicines'])
    return render(request, 'pharma/edit_prescription.html', context={'prescription': pres,
                                                                     'missing_stock': medicines,
                                                                     'all_medicines': all_medicines})
