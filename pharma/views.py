from django.shortcuts import render
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

def place(request):
    if request.method == "GET":
        ID = request.GET['product_id']
        item = Stock.objects.filter(id=ID)[0]
        user = User.objects.filter(username=request.user)[0]
        orders = user.cart.order_set.all()
        in_cart = False
        for order in orders:
            if item == order.product:
                print("in cart")
                in_cart = True
                if item.quantity >= 1:
                    order.quantity += 1
                    item.quantity -= 1
                    item.save()
                    order.save()
                break
        
        if not in_cart:
            if item.quantity >= 1:
                order = Order(quantity=item.quantity, user=user.staff, item=item)
                order.save()
                item.save()
                user.cart.order_set.add(order)
                item.quantity -= 1
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
    print(cart)
    total = get_cart_total(cart)
    orders = cart.order_set.all()
    return render(request, "pharma/cart.html", {'cart' : cart})

def get_total(order):
    return order.quantity * order.product.cost


def get_cart_total(cart):
    orders = cart.order_set.all()
    total = 0
    for order in orders:
        total += get_total(order)

    return total

def bill(request):
    user = User.objects.filter(username=request.user.username)[0]
    orders = user.cart.order_set.all()
    total = get_cart_total(user.cart)
    return render(request, 'pharma/bill.html', {'orders': orders, 'total':total})
