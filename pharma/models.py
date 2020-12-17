from django.db import models


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
