from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.loginPage,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('update',views.update,name='update'),
    path('view',views.viewProfile,name='view'),
    path('list',views.UserListView.as_view(),name='user_list'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', views.change_password, name='password_change'),
    
    ]