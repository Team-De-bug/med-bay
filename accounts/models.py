from django.db import models


# Create your models here.
class Entries(models.Model):

    type_choices = [(True, "income"), (False, "expense")]

    date = models.DateField()
    desc = models.TextField()
    cat = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    type = models.BooleanField(choices=type_choices)

    def __str__(self):
        return f'{self.cat}, {self.desc}, {self.price}'
