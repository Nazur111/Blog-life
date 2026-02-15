from django.urls import path
from .views import article_list, article_create, article_edit, article_delete
from . import views

urlpatterns = [
    path('', article_list, name='articles'),
    path('create/', article_create, name='article_create'),
    path('edit/<int:pk>/', article_edit, name='article_edit'),
    path('delete/<int:pk>/', article_delete, name='article_delete'),
    path('like/<int:pk>/', views.toggle_like, name='toggle_like'),
    path('articles/<int:pk>/publish/', views.article_publish, name='article_publish'),

]


