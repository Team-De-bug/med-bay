from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *
from api.permissions import IsPharma


class ListPrescriptionView(APIView):

    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsPharma]

    def get(self, request):
        prescriptions = Prescription.objects.all()
        serialized = PrescriptionsSerializer(prescriptions, many=True)
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
