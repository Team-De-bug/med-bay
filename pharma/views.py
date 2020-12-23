from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock, Order, Bill, BillUnit
from .forms import StockForm, BillForm


# Create your views here.
@login_required
def shop(request):
    user = User.objects.filter(username=request.user).first()
    if user.staff.role != "p":
        raise PermissionDenied()
    else:
        items = Stock.objects.all()
    items = list(items)
    for item in items:
        if item.quantity < 1:
            items.remove(item)
    return render(request, "pharma/shop.html", context={'items': items})


# Placing order when order button is pressed
@login_required()
def place(request):
    if request.method == "GET":
        ID = request.GET['product_id']
        qty = int(request.GET['product_amount'])
        item = Stock.objects.filter(id=ID)[0]
        user = User.objects.filter(username=request.user)[0]
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

    if request.method == "GET":
        ID = int(request.GET['product_id'])
        reduce = int(request.GET['remove_amount'])
        user = User.objects.filter(username=request.user)[0]
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
    if request.method == "GET":
        ID = int(request.GET['product_id'])
        increase = 1
        user = User.objects.filter(username=request.user)[0]
        item = Stock.objects.filter(id=ID)[0]
        order = user.staff.order_set.filter(item__id=item.id)[0]
        order.quantity += increase
        item.quantity -= increase
        order.save()
        item.save()
    return render(request, "pharma/cart.html", {'cart': cart})


@login_required()
def cart(request):
    if request.method == "POST":
        cq = int(request.POST['qty'])
        order = Order.objects.filter(id=request.POST['order_id'])[0]
        item = Stock.objects.filter(id=order.product.id)[0]

        print(order, item)
        if item.quantity > cq > 1:
            change = int(request.Post['qty']) - order.quantity
            order.quantity = int(request.Post['qty'])
            item.quantity -= change
            order.save()
            item.save()
        
        else:
            user = User.objects.filter(username=request.user)[0]
            print(user)
            cart = user.staff
            cart = cart[0].order_set.all()
            print(cart)
            
            return render(request, "pharma/cart.html", {'cart': cart})

    user = User.objects.filter(username=request.user)[0]
    cart = user.staff
    orders = cart.order_set.all()
    print(cart)
    total = get_total(cart)
    return render(request, "pharma/cart.html", {'cart': orders, 'total': total})


# Getting cart total
def get_total(cart):
    total = 0
    # looping through all the orders in the cart and summing the prices
    for order in cart.order_set.all():
        total += order.quantity * order.item.price
    return total


def bill_info(request):
    if request.method == "POST":
        form = BillForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            # Redirecting user to prescription page
            response = redirect('bill')
            response['Location'] += f'?name={name}&phone={phone}'
            return response

    else:
        form = BillForm()

    return render(request, "pharma/bill_info.html", context={'form':form})


def bill(request):

    # Getting the orders
    user = User.objects.get(username=request.user)
    orders = user.staff.order_set.all()
    print(orders)
    print(request.GET)

    # Generating the bill objects
    bill = Bill(name=request.GET["name"], contact_num=request.GET["phone"], date=timezone.now())
    bill.save()

    for order in orders:
        unit = BillUnit(name=order.item.name, quantity=order.quantity,
                        desc=order.item.desc, price=order.item.price,
                        bill=bill)
        unit.save()
        order.delete()

    bill_units = bill.billunit_set.all()
    print(bill_units, bill)
    return render(request, 'pharma/bill.html', context={'bill': bill, 'bill_unit': bill_units})


@login_required()
def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']

            stock = Stock.objects.create(name=name, desc="med", price=price, quantity=quantity)
            stock.save()

    return render(request, 'pharma/add_stock.html')


@login_required()
def remove_stock(request):
    items = Stock.objects.all()
    items = list(items)
    return render(request, 'pharma/remove_stock.html', context={'items': items})
