from django.urls import path
from .views import get_canvas

urlpatterns = [
    path('canvas/', get_canvas)
]