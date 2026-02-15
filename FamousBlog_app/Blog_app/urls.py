from django.urls import path
from .views import home, toggle_like

app_name = 'blog'  # <-- обов'язково

urlpatterns = [
    path('', home, name='home'),
    path("toggle-like/<int:pk>/", toggle_like, name="toggle_like"),
]