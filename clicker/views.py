from django.shortcuts import get_object_or_404, render, HttpResponse
import datetime


# Create your views here.


def clicker(request):
    return render(request, 'clicker/clicker.html')





