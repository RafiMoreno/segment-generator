from django.urls import path
from .views import get_canvas, get_segments

urlpatterns = [
    path('canvas/', get_canvas),
    path('segments/', get_segments)
]