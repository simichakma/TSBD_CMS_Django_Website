from django.urls import path
from . import views

urlpatterns = [
    path("", views.service_list, name="service_list"),
    path("save/", views.service_save, name="service_save"),
    path("delete/<int:service_id>/", views.service_delete, name="service_delete"),
]
