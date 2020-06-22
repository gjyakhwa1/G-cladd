from django.urls import path
from .views import *

urlpatterns=[
             path('',OrderListView.as_view(),name='order_list'),
             path('<int:pk>/',OrderDetailView.as_view(),name='order_detail'),
             path('<int:pk>/approveQuotation/',approveQuotationView,name='order_approve_quotation'),
             path('<int:pk>/confirmOrder/',confirmOrderView,name='order_confirm'),
             path('<int:pk>/confirmPayment/',confirmPaymentView,name='order_payment_confirm'),
             path('<int:pk>/add<str:type>/',addDnCnView,name='add_dn_cn'),
             path('Puchase/',purchase_confirm,name='confirm_purchase'),
             path('<str:mode>/',quotation_confirm,name='order_confirm_quotation'),
             ]
