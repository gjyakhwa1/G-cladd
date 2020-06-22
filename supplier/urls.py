from .views import SupplierCreateView,SupplierListView,SupplierUpdateView,SupplierDetailView,SupplierDeleteView
from django.urls import path

urlpatterns=[
    path('add/',SupplierCreateView.as_view(),name='supplier_add'),
    path('',SupplierListView.as_view(),name='supplier_list'),
    path('<int:pk>/update/',SupplierUpdateView.as_view(),name='supplier_update'),
    path('<int:pk>/detail/',SupplierDetailView.as_view(),name='supplier_detail'),
    path('<int:pk>/delete/',SupplierDeleteView.as_view(),name='supplier_delete'),
    ]