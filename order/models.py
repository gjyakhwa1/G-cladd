from django.db import models
from product.models import ProductRegister
from django.contrib.auth.models import User
from django.urls import reverse
from project.models import ProjectRegister
from datetime import datetime

# Create your models here.
class OrderRegister(models.Model):
    TYPE_CHOICE=(('Sale','Sale'),('Rent','Rent'),('Purchase','Purchase'))
    STATUS_CHOICE=(('ORDERED','ORDERED'),
                   ('APPROVED','APPROVED'),
                   ('CONFIRMED','CONFIRMED'),
                   ('PACKING','PACKING'),
                   ('SHIPPED','SHIPPED'),
                   ('RETURNED','RETURNED'),
                   ('RECEIVED','RECEIVED'),
                   ('CLOSED','CLOSED'),
                   ('PURCHASED','PURCHASED'),)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(ProjectRegister,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=20,choices=TYPE_CHOICE)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    discount_rate=models.DecimalField(max_digits=5,decimal_places=3,default=0)
    discount_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_advance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_total =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_received =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_due =models.DecimalField(max_digits=10,decimal_places=2,default=0)


    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default='ORDERED',choices=STATUS_CHOICE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.discount_amount=self.total_price*self.discount_rate/100
        self.payment_total=self.total_price-self.discount_amount
        self.payment_due=self.payment_total-self.payment_received
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return f'{self.user.username},{self.id},{self.total_price}'

    def get_absolute_url(self):
        return reverse('order_detail',args=[self.id])
    class Meta:
        ordering=['-timestamp',]

class DnCnRegister(models.Model):
    
    order_register=models.ForeignKey(OrderRegister,on_delete=models.CASCADE)
    timestamp=models.DateField(auto_now_add=True)
    type=models.CharField(max_length=20,choices=(('DN','Delivery Note'),('CN','Collection Note')))
    truck_type=models.CharField(max_length=20)
    truck_rate=models.DecimalField(max_digits=10,decimal_places=2)
    truck_plate_num=models.CharField(max_length=20)
    remarks=models.CharField(max_length=200)
    
    recorded_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order_register.id},{self.recorded_by},{self.order_register.type},{self.type}'



class OrderItemsRegister(models.Model):
    order_register=models.ForeignKey(OrderRegister,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductRegister,on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    sub_total=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'{self.order_register.id},{self.quantity},{self.product_price}'

class RentalDetails(models.Model):
    order_register=models.OneToOneField(OrderRegister,on_delete=models.CASCADE)
    ordered_date=models.DateField(default=datetime.now)
    expected_duration=models.PositiveIntegerField()
    returned_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.order_register.id},{self.ordered_date}'



   

