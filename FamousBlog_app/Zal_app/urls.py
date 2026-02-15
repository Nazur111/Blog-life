from django.urls import path
from . import views

app_name = "sport"

urlpatterns = [
    path('', views.index, name='index'),
]