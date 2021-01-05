from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path('entries', views.entries, name='entries')
]