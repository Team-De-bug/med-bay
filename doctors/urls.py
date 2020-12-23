from django.urls import path
from . import views

urlpatterns = [
    path("", views.appointment, name="appointments"),
    path("case_archive", views.case_archive, name="prescriptions"),
    path("prescription", views.prescription, name="prescription"),
    path("add-prescription", views.add_prescription, name="add-prescription"),
    path("list_medicines", views.list_medicines, name="list_medicines"),
    path("save_prescription", views.save_prescription, name="save_prescription")
]
