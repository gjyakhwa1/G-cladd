from django.contrib import admin
from .models import OrderItemsRegister,OrderRegister,DnCnRegister,RentalDetails
# Register your models here.
admin.site.register(OrderRegister)
admin.site.register(OrderItemsRegister)
admin.site.register(DnCnRegister)
admin.site.register(RentalDetails)