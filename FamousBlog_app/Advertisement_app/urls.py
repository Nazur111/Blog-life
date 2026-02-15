from django.urls import path
from . import views

urlpatterns = [
    path('', views.head_page, name='head'),  
    path('create/', views.advert_create, name='advert_create'),
    path('delete/<int:pk>/', views.advert_delete, name='advert_delete'),
    path('edit/<int:pk>/', views.advert_edit, name='advert_edit'),
]

