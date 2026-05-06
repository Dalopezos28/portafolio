from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, WorkExperience, Skill


def home(request):
    experiences = WorkExperience.objects.all()
    skills = Skill.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:3]
    if not featured_projects.exists():
        featured_projects = Project.objects.all()[:3]
    return render(request, 'portfolio/home.html', {
        'experiences': experiences,
        'skills': skills,
        'featured_projects': featured_projects,
    })


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
