from django.db import models
from django.contrib.auth.models import User

roles = (("d", "doctor"), ("p", "pharma manager"), ("a", "admin/front_desk"),
         ("ac", "accounts"))


# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=20, choices=roles)

    def __str__(self):
        return f"{self.user.username}"
