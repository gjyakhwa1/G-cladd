from django.urls import path
from . import views

urlpatterns=[path('add/',views.ProjectCreateView.as_view(),name='project_add'),
            path('<int:pk>/',views.ProjectDetailView.as_view(),name='project_detail'),
            path('<int:pk>/update',views.ProjectUpdateView.as_view(),name='project_update'),    
            path('<int:pk>/delete',views.ProjectDeleteView.as_view(),name='project_delete'),
            path('',views.ProjectListView.as_view(),name='project_list'),
]