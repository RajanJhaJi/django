from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.


def projects(request):
    projectlist = Project.objects.all()
    # print(f'this is the obect we are getting {object}')
    return render(request,'projects/projects.html',{"projectslist":projectlist})


def project(request,pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    # print(f'this is the obect we are getting {object}')
    return render(request,'projects/project.html',{"project":project,"tags":tags})

def createproject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")
    # print(f'this is the obect we are getting {object}')
    return render(request,'projects/project-form.html',{"form":form})

def updateproject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,instance=project) #WE ADD INSTANCE HERE ALSO TO UPDATE THE PROJECT ELSE IT  WILL CREATE A NEW PROJECT
        if form.is_valid():
            form.save()
            return redirect("projects")
    # print(f'this is the obect we are getting {object}')
    return render(request,'projects/project-form.html',{"form":form})

def deleteproject(request,pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect("projects")

