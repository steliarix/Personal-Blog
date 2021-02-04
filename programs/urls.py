from django.urls import path, include
from . import views

urlpatterns = [
    path('programs/', views.index_programs, name='home_programs'),
    path('programs/', include('news.urls')),
    path('programs/', include('clicker.urls')),
    path('programs/', include('weather.urls')),
    path('programs/', include('todo.urls')),
    path('programs/', include('notes.urls')),
]
