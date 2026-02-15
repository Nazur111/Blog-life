from django.urls import path
from . import views

app_name = "technology"

urlpatterns = [
    path('', views.index, name='index'),
]



