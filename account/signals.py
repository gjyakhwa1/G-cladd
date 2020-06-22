from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
from project.models import ProjectRegister
from .models import Company

@receiver(pre_save,sender=ProjectRegister)
def update_project(sender,instance ,args,**kwargs):
    project=ProjectRegister.objects.get(id=instance.id)

    if instance.company!=None:
        instance.company.payment_total-=project.payment_total
        instance.company.payment_total+=instance.payment_total

        instance.company.payment_received-=project.payment_received
        instacnce.company.payment_received+=instance.payment_received

        instance.company.save()
   
@receiver(pre_delete,sender=ProjectRegister)
def delete_project(sender,instance,args,**kwargs):
    if instance.company != None:
        instance.company.payment_total-=instance.payment_total
        instance.company.payment_received-=instance.payment_received
        instance.company.save()


