from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock
from admins.models import Staff

# Create your views here.
def shop(request):
    items = Stock.objects.all()
    return render(request, "pharma/shop.html", context={'items':items})
   
def place(request):
    if request.method == "GET":
        ID = request.GET['id']
        item = Stock.objects.filter(id=ID)
        item = item[0]
        user = User.objects.filter(username=request.user)
        user = user[0]
        if user.staff.role == "p":
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
    return HttpResponse("success")