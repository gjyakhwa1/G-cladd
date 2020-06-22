from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import SupplierRegister
from .forms import addSupplierForm
from .filters import SupplierFilter
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.
class SupplierCreateView(SuccessMessageMixin,generic.CreateView):
    model=SupplierRegister
    form_class=addSupplierForm
    template_name='supplier/supplier_add.html'
    
    success_message=" Supplier Added Successfully !!"

    def get_initial(self):
        initial= super().get_initial()
        initial['recorded_by']=self.request.user
        return initial

    

class SupplierListView(generic.ListView):
    model=SupplierRegister
    context_object_name='supplier_list'
    template_name='supplier/supplier_list.html'
    paginate_by = 10

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=SupplierFilter(self.request.GET,self.get_queryset())
        return context

class SupplierUpdateView(SuccessMessageMixin,generic.UpdateView):
    model=SupplierRegister
    form_class=addSupplierForm
    template_name='supplier/supplier_update.html'
    success_message="Supplier Details Updated Successfully !!!"
    

    

class SupplierDetailView(generic.DetailView):
    model=SupplierRegister
    template_name='supplier/supplier_detail.html'
    context_object_name='supplier'

    

class SupplierDeleteView(SuccessMessageMixin,generic.DeleteView):
    model=SupplierRegister
    template_name='supplier/supplier_delete.html'
    success_url=reverse_lazy('dashboard')
    success_message='Supplier Deleted Successfully !!!'
    context_object_name='supplier'

    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super().delete(request, *args, **kwargs)
    
        

