from django.urls import path, include
from pharma import api_views
from rest_framework.authtoken import views
from .views import ping, csrf

urlpatterns = [
   path('api-token-auth/', views.obtain_auth_token),
   path('api-auth/', include('rest_framework.urls')),
   path('last-pres', api_views.LastPrescriptionView.as_view()),
   path('stock', api_views.ListStockView.as_view()),
   path('csrf', csrf),
   path('ping', ping),
]
