from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("save/", views.project_save, name="project_save"),
    path("delete/<int:project_id>/", views.project_delete, name="project_delete"),
]
