from django.urls import path, include
from . import views

urlpatterns = [
    path('todo/', views.todo, name='todo')
]
