from django.shortcuts import render
from projects.models import Project
from titles.models import Title
from django.http import HttpResponse


def index(request):
    projects = Project.objects.values("id", "name", "description", "url").all()
    titles = Title.objects.all()
    return render(request, "mainapp/index.html", {"projects": projects, "titles": titles})

