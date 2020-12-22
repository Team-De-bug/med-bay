from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("place", views.place, name="shop"),
    path("remove", views.remove, name="cart"),
    path("add_one", views.add_one, name="cart"),
    path("cart", views.cart, name="cart")
]
