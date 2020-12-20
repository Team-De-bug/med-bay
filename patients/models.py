from django.db import models
from doctors.models import Doctor


# Patient model.
class Patient(models.Model):
    # Choice list
    blood_types = (("A+", "A+"), ("B+", "B+"), ("O+", "O+"), ("AB+", "AB+"),
                   ("A-", "A-"), ("B-", "B-"), ("O-", "O-"), ("AB-", "AB-"))
    gender_list = (("M", "male"), ("F", "female"), ("T", "trans"))

    # Fields
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gender_list)
    blood_type = models.CharField(max_length=5, choices=blood_types)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f"{self.id}: {self.name}"


# Created when a visit is done
class Cases(models.Model):
    # Choices list
    states = (("e", "Emergency"), ("n", "Normal"), ("c", "Checkup"))
    status_options = (("t", "ToDo"), ("i", "in progress"), ("d", "done"))

    # Fields
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    desc = models.TextField()
    appointed_date = models.DateTimeField("appointment date")
    state = models.CharField(max_length=3, choices=states)
    status = models.CharField(max_length=3, choices=status_options)

    def __str__(self):
        return f'case_id: {self.id}'
