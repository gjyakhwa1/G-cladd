from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class ProductRegister(models.Model):
    productName= models.CharField(max_length=100)
    productItemCode= models.CharField(max_length=100)
    productBrandNewSellingRate= models.DecimalField(max_digits=10, decimal_places=2)
    productSecondHandSellingRate= models.DecimalField(max_digits=10, decimal_places=2)
    productLossRate=models.DecimalField(max_digits=10, decimal_places=2)
    productRepairRate=models.DecimalField(max_digits=10, decimal_places=2)
    productCleaningRate=models.DecimalField(max_digits=10, decimal_places=2)
    productDailyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    productWeeklyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    productMonthlyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    productDailyHireCharge=models.DecimalField(max_digits=10, decimal_places=2)
    productWeeklyHireCharge=models.DecimalField(max_digits=10, decimal_places=2)
    productMonthlyHireCharge=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    productRecordedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    #supplierName=models.TextField(blank=True)
    remarks=models.CharField(max_length=200)
    image=models.ImageField(default='product_pics/default.png',upload_to='product_pics')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id])

    def get_update_url(self):
        return reverse('product_update',args=[self.id])

    def get_delete_url(self):
        return reverse('product_delete',args=[self.id])

    def __str__(self):
        return self.productName

    def save(self):
        self.productName=self.productName.capitalize()
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        ordering=['productName']