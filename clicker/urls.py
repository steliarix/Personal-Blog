from django.urls import path, include
from . import views

urlpatterns = [
    path('clicker/', views.clicker, name='clicker')
]
