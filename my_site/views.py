from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from account.models import Company
from .forms import AddCompanyForm
from django.urls import reverse_lazy
from .filters import CompanyFilter
from product.models import ProductRegister
from order.models import OrderRegister,OrderItemsRegister
from project.models import ProjectRegister
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def dashboard(request):
    
    return render(request,'dashboard.html',{})

def inventoryView(request):
    context={}
    total_items=0
    
    if request.user.profile.company.type == "self":
        inventory_self=ProductRegister.objects.all()
        for a in inventory_self:
            total_items+=a.stock
        print(total_items)
        context['inventory_self']=inventory_self
        context['total_items']=total_items
    elif request.user.profile.company.type=='client':
        inventory_client={}
        projects=ProjectRegister.objects.filter(company=request.user.profile.company)
        orders=OrderRegister.objects.filter(Q(project__in = projects)
                                           & 
                                            ((Q(status__in=['SHIPPED','CLOSED']) & Q(type='Sale')))
                                             |
                                             (Q(status__in=['SHIPPED']) & Q(type='Rent'))
                                             )
        #rental_orders=OrderRegister.objects.filter(Q(type='Rent') & Q(status='CLOSED'))
        #print(rental_orders)
        
        #orders.difference(rental_orders)
        print(orders)
        for order in orders:
            orderRegisterItems=OrderItemsRegister.objects.filter(order_register=order)

            for orderRegisterItem in orderRegisterItems:
                product=orderRegisterItem.product
                quantity=orderRegisterItem.quantity
                total_items+=quantity
                exist=inventory_client.get(product)
                if exist :
                    quantity+=exist['quantity']
                   
                
                inventory_client[product]={'product':product,
                                                       'quantity':quantity}
                

       

        context['inventory_client']=inventory_client
        context['total_items']=total_items
        
    return render(request,'inventory.html',context)


class CompanyCreateView(SuccessMessageMixin,generic.CreateView):
    model=Company
    form_class=AddCompanyForm
    
    success_message="Company Successfully Created "
    template_name='company/company_add.html'
    

class CompanyUpdateView(SuccessMessageMixin,generic.UpdateView):
    model=Company
    form_class=AddCompanyForm
    success_message="Company Successfully Updated"
    template_name='company/company_update.html'
    

class CompanyListView(generic.ListView):
    model=Company
    paginated_by=10
    context_object_name='company_list'
    template_name='company/company_list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filter']=CompanyFilter(self.request.GET,self.get_queryset())
        return context

class CompanyDetailView(generic.DetailView):
    model=Company
    context_object_name='company'
    template_name='company/company_detail.html'

    def dispatch(self, request, *args, **kwargs):
        company = self.get_object()
        if self.request.user.profile.account_type not in ['SA','SU']:
             if self.request.user.profile.company !=company:
                 return HttpResponseForbidden('Access Denied')
        return super(CompanyDetailView, self).dispatch(request, *args, **kwargs)
        

   

    




class CompanyDeleteView(SuccessMessageMixin,generic.DeleteView):
    model=Company
    context_object_name='company'
    template_name='company/company_delete.html'
    success_message="Company Deleted Successfully"
    success_url=reverse_lazy('company_list')
    
   

    

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)