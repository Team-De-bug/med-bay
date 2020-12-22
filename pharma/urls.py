from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("cart", views.cart, name="cart")
]
