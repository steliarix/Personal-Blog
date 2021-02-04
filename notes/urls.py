from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.notes, name='notes')
]
