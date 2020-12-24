from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path("", views.appointment, name="dashboard"),
    path("case_archive", views.case_archive, name="case_archive"),
    path("recover", views.prescription, name="recover"),
    path("add_prescription", views.add_prescription, name="add_prescription"),
    path("list_medicines", views.list_medicines, name="list_medicines"),
    path("save_prescription", views.save_prescription, name="save_prescription")
]
