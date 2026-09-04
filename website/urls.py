from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
<<<<<<< HEAD
    path("services/<int:service_id>/", views.service_detail, name="service-detail"),
=======
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
    path("projects/", views.projects, name="projects"),
    path("products/", views.product_list, name="products"),
    path("products/<int:product_id>/", views.product_detail, name="product-detail"),
    path("blog/", views.blog_list, name="blog"),
    path("blog/<int:blog_id>/", views.blog_detail, name="blog-detail"),
<<<<<<< HEAD
    path("team/", views.team, name="team"),
    path("team/<int:member_id>/", views.team_detail, name="team-detail"),
    path("api/team/<int:member_id>/", views.team_member_api, name="team-member-api"),
    path("contact/", views.contact, name="contact"),
=======
    path("team/",views.team,name="team"),
    path("api/team/<slug:member_slug>/", views.team_member_api, name="team-member-api"),
    path("contact/", views.contact, name="contact"),
    # Public member URLs intentionally live at the site root: /member-name/
    path("<slug:member_slug>/", views.team_detail, name="team-detail"),
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
]
