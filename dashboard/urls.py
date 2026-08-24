from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("services/", include("services.urls")),
    path("projects/", include("projects.urls")),
    path("team/",include("team.urls")),
    path("messages/", views.message_list, name="message_list"),
]
