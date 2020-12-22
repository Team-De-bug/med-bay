from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("place", views.place, name="shop"),
    path("cart", views.cart, name="cart")
]
