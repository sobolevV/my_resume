from django.shortcuts import render
# from projects.models import Project
# from titles.models import Title
from django.http import HttpResponse


def index(request):
    # projects = Project.objects.values("id", "name", "description", "url").all()
    # titles = Title.objects.all()
    # {"projects": projects, "titles": titles}
    return render(request, "mainapp/index.html", )


def myhandler404(request, *args, **kwargs):
    return render(request, 'handlers/404.html',  context={'title': '404 Error',
                                                                   'error': '404 Error'})

