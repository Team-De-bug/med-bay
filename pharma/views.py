from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock, Order


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
            if order.item.id == item.id: in_cart = True

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


def remove(request):

    if request.method == "GET":
        ID = request.GET['order_id']
        print(ID)
        order = Order.objects.filter(id=ID)[0]
        item = Stock.objects.filter(id=order.product.id)[0]
        item.quantity += order.quantity
        order.delete()
        item.save()

    return HttpResponse("success")


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
            messages.error(request, f'not possible!')
            
            return render(request, "pharma/cart.html", {'cart' : cart})

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


def bill(request):
    user = User.objects.filter(username=request.user.username)[0]
    orders = user.cart.order_set.all()
    total = get_total(user.cart)
    return render(request, 'pharma/bill.html', {'orders': orders, 'total':total})
