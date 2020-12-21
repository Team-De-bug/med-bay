from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock, Cart
from admins.models import Staff

# Create your views here.
@login_required
def shop(request):
    user = User.objects.filter(username=request.user).first()
    if user.staff.role != "p":
        raise PermissionDenied()
    else:
        items = Stock.objects.all()
        return render(request, "pharma/shop.html", context={'items':items})


def place(request):
    if request.method == "GET":
        ID = request.GET['id']
        item = Stock.objects.filter(id=ID)
        item = item[0]
        user = User.objects.filter(username=request.user)
        user = user[0]
        orders = user.cart.order_set.all()
        in_cart = False
        for order in orders:
            if item == order.product:
                print("in cart")
                in_cart = True
                order.quantity += 1
                order.save()
                break

        if not in_cart:
            order = Order(cart=user.cart, product=item)
            order.save()
            user.cart.order_set.add(order)

"""def remove(request):

    if request.method == "GET":
        ID = request.GET['order_id']
        print(ID)
        order = Order.objects.filter(id=ID)
        order = order[0]
        order.delete()

    return HttpResponse("success")


def cart(request):
    cart = Cart.objects.filter(user=request.user)
    cart = cart[0].order_set.all()
    print(cart)
    return render(request, "sahara/cart.html", {'cart': cart})"""
