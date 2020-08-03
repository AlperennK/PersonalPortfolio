from django.shortcuts import render
from .models import Project
# Create your views here.
"""Grabbing objects from db"""

def home(request):
    projects=Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
