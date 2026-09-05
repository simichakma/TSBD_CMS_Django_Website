from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("services/<int:service_id>/", views.service_detail, name="service-detail"),
    path("projects/", views.projects, name="projects"),
    path("products/", views.product_list, name="products"),
    path("products/<int:product_id>/", views.product_detail, name="product-detail"),
    path("blog/", views.blog_list, name="blog"),
    path("blog/<int:blog_id>/", views.blog_detail, name="blog-detail"),
    path("team/", views.team, name="team"),
    path("team/<int:member_id>/", views.team_detail, name="team-detail"),
    path("api/team/<int:member_id>/", views.team_member_api, name="team-member-api"),
    path("contact/", views.contact, name="contact"),
]
