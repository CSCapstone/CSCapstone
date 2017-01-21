"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from .forms import CreateProjectForm
from .models import Project

def getProjects(request):
    projects_list = []
    try:
        projects_list = Project.objects.all()
    except Exception as ex:
        pass
    return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
    project_id = int(request.GET.get('id'))
    project = Project.objects.filter(project_id=project_id)[0]
    context = {
        "project": project
    }
    return render(request, 'project.html', context)

def getCreateProject(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = CreateProjectForm(request.POST)
            if form.is_valid():
                new_project = Project(
                    name=form.cleaned_data['name'], 
                    description=form.cleaned_data['description'],
                    company=form.cleaned_data['company'],
                    language=form.cleaned_data['language'],
                    experience=form.cleaned_data['experience'],
                    speciality=form.cleaned_data['speciality']
                )
                new_project.save()
                context = {
                    'name' : form.cleaned_data['name'],
                    'project_id' : new_project.project_id
                }
                return render(request, 'projectformsuccess.html', context)
            else:
                return render(request, 'create_project.html', {'error' : 'Error: Project failed to create.'})
        else:
            form = CreateProjectForm()
            context = {
                "form": form,
                "button_value": "Create Project"
            }
            return render(request, 'create_project.html', context)
