from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Stock)
admin.site.register(Prescription)
admin.site.register(Order)
admin.site.register(Medicine)
admin.site.register(Bill)
admin.site.register(BillUnit)
admin.site.register(EditedPrescription)
admin.site.register(EPMedicine)
