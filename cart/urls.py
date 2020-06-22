from django.urls import path
from . import views

urlpatterns=[ path('<str:mode>',views.cartView,name='cart_view'),]