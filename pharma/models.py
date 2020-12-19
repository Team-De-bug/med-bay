from django.db import models
from patients.models import Cases


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


# Prescription
class Prescription(models.Model):
    case = models.OneToOneField(Cases, on_delete=models.SET_NULL, null=True)
    medicines = models.ManyToManyField(Stock)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
