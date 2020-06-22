from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from account.models import Company
# Create your models here.

class ProjectRegister(models.Model):
    STATUS_TYPES=(('Running','Running'),('Completed','Completed'))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    projectTitle=models.CharField(max_length=100)
    projectId=models.IntegerField()
    projectContractNo=models.IntegerField()
    projectSiteLocation=models.CharField(max_length=100)
    projectMailLocation=models.CharField(blank=True,max_length=50)
    orderNumber=models.IntegerField(default=0)
    projectStatus=models.CharField(max_length=100,choices=STATUS_TYPES)
    projectRecordedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    txTruckRates=models.IntegerField()
    payment_total =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_received =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_due =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    remarks=models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.payment_due=self.payment_total-self.payment_received
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.projectTitle
    def save(self):
        self.projectTitle=self.projectTitle.capitalize()
        super().save()
    def get_absolute_url(self):
        return reverse('project_detail',args=[self.id])
    def get_update_url(self):
        return reverse('project_update',args=[self.id])
    def get_delete_url(self):
        return reverse('project_delete',args=[self.id])
    class Meta:
        ordering=['projectTitle',]

