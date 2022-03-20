from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("",views.projects,name="projects"),
    path("projects/add_project",views.createproject,name="addproject"),
    path("projects/update_project/<str:pk>",views.updateproject,name="updateproject"),
    path("projects/delete_project/<str:pk>",views.deleteproject,name="deleteproject"),
    path("project/<str:pk>",views.project,name="project"),
 
]