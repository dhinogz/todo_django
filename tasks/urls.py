from django.urls import path, include
from .views import todo_view

urlpatterns = [
    
    path('', todo_view, name='todo'),
    
]
