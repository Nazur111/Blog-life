from django.urls import path
from . import views

urlpatterns = [
    # приклад
    path('', views.index, name='image_index'),
]
