from django.urls import path, include
from pharma import api_views
from rest_framework.authtoken import views

urlpatterns = [
   path('api-token-auth/', views.obtain_auth_token),
   path('api-auth/', include('rest_framework.urls')),
   path('pres', api_views.ListPrescriptionView.as_view()),
   path('stock', api_views.ListStockView.as_view()),

]
