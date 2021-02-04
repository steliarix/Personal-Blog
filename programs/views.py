from django.shortcuts import render

# Create your views here.

def index_programs(request):
    return render(request, 'programs/programs.html')
