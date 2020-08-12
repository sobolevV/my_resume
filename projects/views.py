from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_description(request, id='1'):
    # if request.method == "POST":
    # request.POST.get("id")
    project_obj = Project.objects.get(id=id)
    return render(request, "projects/project_description.html", {"project": project_obj})