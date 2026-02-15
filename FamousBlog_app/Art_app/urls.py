from django.urls import path
from . import views

app_name = "paint"

urlpatterns = [
    path('', views.index, name='index'),
]