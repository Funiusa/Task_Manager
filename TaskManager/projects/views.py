from django.shortcuts import render
from .models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, template_name="project_index.html", context=context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, template_name="project_detail.html", context=context)
