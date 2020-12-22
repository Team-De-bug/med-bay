from django.urls import path
from . import views

urlpatterns = [
    path("", views.appointment, name="appointments"),
    path("prescriptions", views.prescriptions, name="prescriptions"),
    path("prescription", views.prescription, name="prescription"),
    path("add-prescription", views.addprescription, name="add-prescription")
]
