from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.


class Company(models.Model):
    TYPE_CHOICE = (('self', 'Self'), ('client', 'Client'))
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    type = models.CharField(max_length=10, default='client', choices=TYPE_CHOICE)
    payment_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_received = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contact_number = models.CharField(max_length=15)
    website = models.URLField(blank=True)
    remarks = models.CharField(max_length=255, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.payment_due = self.payment_total-self.payment_received
        self.name = self.name.capitalize()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', args=[self.id])

    def get_update_url(self):
        return reverse('company_update', args=[self.id])

    def get_delete_url(self):
        return reverse('company_delete', args=[self.id])


class Profile(models.Model):
    ACCOUNT_TYPE_CHOICES = (('SA', 'System Admin'), ('SU', 'System User'), ('CA', 'Client Admin'),
                            ('CU', 'Client User'), ('YM', 'Yard Manager'), ('PM', 'Project Manager'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    contact_number = models.CharField(max_length=15)
    account_type = models.CharField(max_length=15, choices=ACCOUNT_TYPE_CHOICES)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    profile_picture = models.ImageField(default='profile_pics/avatar.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} /{self.company.name}/{self.account_type}'

    def save(self):
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
