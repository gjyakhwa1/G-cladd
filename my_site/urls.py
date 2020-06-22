from django.urls import include,path
from .views import *
from django.views.generic import RedirectView

urlpatterns=[
    #path('',RedirectView.as_view(url='dashboard/')),
    path('',dashboard,name='dashboard'),
    path('product/',include('product.urls')),
    path('supplier/',include('supplier.urls')),
    path('project/',include('project.urls')),
    path('account/',include('account.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    path('inventory/',inventoryView,name='inventory'),
    path('company/add',CompanyCreateView.as_view(),name='company_add'),
    path('company/<int:pk>/update',CompanyUpdateView.as_view(),name='company_update'),
    path('company/',CompanyListView.as_view(),name='company_list'),
    path('company/<int:pk>/',CompanyDetailView.as_view(),name='company_detail'),
    path('company/<int:pk>/delete',CompanyDeleteView.as_view(),name='company_delete'),
    
    ]
