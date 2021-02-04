from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', include('programs.urls')),
    path('aboutme/', views.about, name='about_me_page'),
    path('contacts/', views.contacts, name='contacts')
]
