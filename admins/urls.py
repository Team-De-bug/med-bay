from django.urls import path
from . import views

app_name = 'admins'
urlpatterns = [
    path('attendance', views.attendance, name="attendance"),
    path('create_patient', views.create_patient, name="create_patient")
]
