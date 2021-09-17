from django.urls import path
from pharma import api_views

urlpatterns = [
   path('pres', api_views.ListPrescriptionView.as_view())
]
