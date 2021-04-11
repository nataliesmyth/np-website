from typing import ContextManager
from django.shortcuts import render
from home.models import Home

def home_index(request):
    projects = Home.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'home_index.html', context)

def home_detail(request, pk):
    projects = Home.objects.get(pk=pk)
    context = {
        'projects': projects
    }
    return render(request, 'home_detail.html', context)