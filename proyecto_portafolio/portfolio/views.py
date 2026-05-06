# portfolio/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    