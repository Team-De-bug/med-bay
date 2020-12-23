from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("place", views.place, name="place"),
    path("remove", views.remove, name="remove"),
    path("add_one", views.add_one, name="add"),
    path("add_stock", views.add_stock, name="update"),
    path("cart", views.cart, name="cart")
]
