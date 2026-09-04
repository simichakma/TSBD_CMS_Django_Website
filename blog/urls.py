from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.blog_list,
        name="blog-list"
    ),

    path(
        "add/",
        views.add_blog,
        name="add-blog"
    ),

    path(
        "edit/<int:blog_id>/",
        views.edit_blog,
        name="edit-blog"
    ),

    path(
        "delete/<int:blog_id>/",
        views.delete_blog,
        name="delete-blog"
    ),

]