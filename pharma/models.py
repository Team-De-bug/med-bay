from django.db import models
from patients.models import Cases


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)


# Prescription
class Prescription(models.Model):
    case = models.ForeignKey(Cases, on_delete=models.SET_NULL, null=True)
    medicines = models.ManyToManyField(Stock)
    status = models.BooleanField(default=False)
