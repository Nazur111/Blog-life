from django.urls import path
from . import views  # Переконайся, що views.py існує

app_name = "categorys"
urlpatterns = [
    path('', views.category_list, name='category_list'),
]

