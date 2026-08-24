from django.urls import path
from . import views


urlpatterns = [

    path("",views.product_list,name="product-list"),

    path("add/",views.add_product,name="add-product"),

    path("edit/<int:product_id>/",views.edit_product,name="edit-product"),

    path( "delete/<int:product_id>/",views.delete_product,name="delete-product"),

]