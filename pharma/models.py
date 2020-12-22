from django.db import models
from admins.models import Staff
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

    status_list = (("c", "Created"), ('p', 'Prescribed'), ('d', 'Delivered'))

    case = models.OneToOneField(Cases, on_delete=models.SET_NULL, null=True)
    medicines = models.ManyToManyField(Stock)
    status = models.CharField(default='c', max_length=2, choices=status_list)

    def __str__(self):
        return f'{self.id}'


# Orders unit
class Order(models.Model):

    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.user.username}, {self.item.name}'


# Medicine in prescription
class Medicine(models.Model):

    case = models.ForeignKey(Cases, on_delete=models.CASCADE)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.user.username}, {self.item.name}'
