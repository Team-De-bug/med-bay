from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import PrescriptionsSerializer
from .models import *


class ListPrescriptionView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        prescriptions = Prescription.objects.all()
        serialized = PrescriptionsSerializer(prescriptions, many=True)
        return Response(serialized.data)
