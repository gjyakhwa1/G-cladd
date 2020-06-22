from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class SupplierRegister(models.Model):
    supplierName=models.CharField(max_length=100)
    supplierAddress=models.CharField(max_length=100)
    supplierUrl=models.URLField(max_length=2083)
    supplierContactPerson=models.CharField(max_length=100)
    supplierContact1=models.CharField(max_length=30)
    supplierContact2=models.CharField(max_length=30)
    supplierContactFax=models.CharField(max_length=100)
    supplierEmail=models.EmailField(max_length=100)
    recorded_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.supplierName
    
    def get_update_url(self):
        return reverse('supplier_update',args=[self.id])

    def get_absolute_url(self):
        return reverse('supplier_detail',args=[self.id])
    def get_delete_url(self):
        return reverse('supplier_delete',args=[self.id])
    def save(self):
        self.supplierName=self.supplierName.capitalize()
        super().save()

    class Meta:
        ordering=['supplierName']
    

  