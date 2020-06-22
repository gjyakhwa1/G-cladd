from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
from order.models import OrderRegister


@receiver(pre_save,sender=OrderRegister)
def pre_update_order(sender,instance,**kwargs):
    try:
        register=OrderRegister.objects.get(id=instance.id)
        if register.project==None and not instance.project==None:
            #project is assigned to the given order register entity
            print('Project Assigned')
            instance.project.payment_total+=instance.payment_total
            instance.project.company.payment_total+=instance.payment_total
            instance.project.company.save()
            instance.project.save()
            
            
        else:
            added_payment_total=instance.payment_total-register.payment_total
            instance.project.company.payment_total+=added_payment_total
            instance.project.payment_total+=added_payment_total

            added_payment_received=instance.payment_received-register.payment_received
            instance.project.company.payment_received+=added_payment_received
            instance.project.payment_received+=added_payment_received

            instance.project.company.save()
            instance.project.save()

            #instance.project.payment_total-=register.payment_total
            #instance.project.payment_total+=instance.payment_total 

            #instance.project.payment_received-=register.payment_received
            #instance.project.payment_received+=instance.payment_received
            
            
            #instance.project.save()
    except:
        print('Project not assigned yet')

@receiver(pre_delete,sender=OrderRegister)
def delete_order(sender,instance,**kwargs):
    if instance.project != None:
        instance.project.payment_total-=instance.payment_total
        instance.project.company.payment_total-=instance.payment_total

        instance.project.payment_received-=instance.payment_received
        instance.project.company.payment_received-=instance.payment_received
        
        instance.project.company.save()
        instance.project.save()
        