from django.db import models
from admins.models import Staff
from patients.models import Cases


# Create your models here.
class Stock(models.Model):

    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


# Bill
class Bill(models.Model):

    name = models.CharField(max_length=50)
    contact_num = models.CharField(max_length=10)
    date = models.DateTimeField()

    def __str__(self):
        return f'bill-id: {self.id}| date: {self.date}'


# Prescription
class Prescription(models.Model):

    status_list = (("c", "Created"), ('p', 'Prescribed'), ('d', 'Delivered'))

    bill = models.OneToOneField(Bill, on_delete=models.SET_NULL, null=True)
    case = models.OneToOneField(Cases, on_delete=models.SET_NULL, null=True)
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

    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.prescription.id},{self.item.name}, {self.quantity}'


class EditedPrescription(models.Model):

    pres = models.OneToOneField(Prescription, on_delete=models.CASCADE)
    user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"pres: {self.pres.id} edited by {self.user.user.username}"


# Medicine in prescription
class EPMedicine(models.Model):

    prescription = models.ForeignKey(EditedPrescription, on_delete=models.CASCADE, related_name='medicines')
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.prescription.id},{self.item.name}, {self.quantity}'


# part of the bill
class BillUnit(models.Model):

    bill = models.ForeignKey(Bill, models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
