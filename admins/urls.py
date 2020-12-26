from django.urls import path
from . import views

app_name = 'admins'
urlpatterns = [
    path('attendance', views.attendance, name="attendance"),
    path('create_patient', views.create_patient, name="create_patient"),
    path('edit_patient', views.edit_patient, name="edit_patient"),
    path('create_cases', views.create_case, name="create_case"),
    path('edit_cases', views.edit_case, name="edit_case"),
    path('list_patients', views.list_patients, name="list_patients"),
    path('list_cases', views.list_cases, name="list_cases")
]
