from django.db import models

blood_types = (("A+", "A+"), ("B+", "B+"), ("O+", "O+"), ("AB+", "AB+"),
               ("A-", "A-"), ("B-", "B+"), ("O-", "O+"), ("AB-", "AB-"))
gender_list = (("m", "male"), ("f", "female"), ("t", "trans"))


# Patient model.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gender_list)
    blood_type = models.CharField(max_length=5, choices=blood_types)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default=None)
