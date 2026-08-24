from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("projects/", views.projects, name="projects"),
    path("products/", views.product_list, name="products"),
    path("products/<int:product_id>/", views.product_detail, name="product-detail"),
    path("blog/", views.blog_list, name="blog"),
    path("blog/<int:blog_id>/", views.blog_detail, name="blog-detail"),
    path("team/",views.team,name="team"),
    path("api/team/<slug:member_slug>/", views.team_member_api, name="team-member-api"),
    path("contact/", views.contact, name="contact"),
    # Public member URLs intentionally live at the site root: /member-name/
    path("<slug:member_slug>/", views.team_detail, name="team-detail"),
]
