from rest_framework import serializers
from . import models


class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        exclude = ['deleted']
