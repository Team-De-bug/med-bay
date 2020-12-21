from django.db import models
from patients.models import Cases
from admins.models import Staff

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

    status_list = (("c", "Created"), ('p', 'Prescribed'), ('d', 'Delivered'))

    case = models.OneToOneField(Cases, on_delete=models.SET_NULL, null=True)
    medicines = models.ManyToManyField(Stock)
    status = models.CharField(default='c', max_length=2, choices=status_list)

    def __str__(self):
        return f'{self.id}'

class Cart(models.Model):
    user = models.OneToOneField(Staff, on_delete=models.CASCADE)
    items = models.IntegerField(default=0, name="items")

    def __str__(self):
        return f'{self.user.username} cart'