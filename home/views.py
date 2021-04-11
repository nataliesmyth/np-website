from django.shortcuts import render
from home.models import Home

def home_index(request):
    projects = Home.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'home_index.html', context)