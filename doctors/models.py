from django.db import models
from admins.models import Staff


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(Staff, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50)
    availability = models.BooleanField(default=False)
    visit_cost = models.IntegerField(default=0)
