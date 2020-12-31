from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("", views.home, name='home'),
    path('entries', views.entries, name='entries')
]