from django.urls import path
from .import views
urlpatterns=[
    path('add/',views.ProductCreate.as_view(),name='product_add'),
    path('',views.ProductListView.as_view(),name='product_list'),
    path('<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('<int:pk>/update/',views.ProductUpdateView.as_view(),name='product_update'),
    path('<int:pk>/delete/',views.ProductDeleteView.as_view(),name='product_delete'),
    #path('add/',views.product_add,name='product_add'),
    ]