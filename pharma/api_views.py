from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *
from api.permissions import IsPharma
from patients.models import Patient


class LastPrescriptionView(APIView):

    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsPharma]

    def get(self, request):
        patient_id = request.GET['patient_id']

        # Getting the patient using the id
        try:
            patient = Patient.objects.get(id=patient_id)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Getting prescription
        case = list(patient.cases_set.all().order_by('appointed_date'))[-1]
        print(case)
        prescription = case.prescription

        # Getting medicines from prescription
        medicines = prescription.medicine_set.all()
        serialized = MedicineSerializer(medicines, many=True)

        return Response(serialized.data)


class ListStockView(APIView):

    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsPharma]

    def get(self, request):
        stock = Stock.objects.all()
        valid = []
        for objects in stock:
            if objects.quantity > 0 and not objects.deleted:
                valid.append(objects)

        serialized = StockSerializer(valid, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = StockSerializer(request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)
