from django.urls import path
from . import views

urlpatterns = [
    path('attendance', views.attendance, name="attendance")
]
