from django.urls import path
from . import views


urlpatterns = [

    path('',views.team_list,name='team-list'),

    path('data/', views.team_data, name='team-data'),

    path('add/',views.add_team,name='add-team'),

    path('get/<int:team_id>/',views.get_team,name='get-team'),

    path('edit/<int:team_id>/',views.edit_team,name='edit-team'),

    path('delete/<int:team_id>/',views.delete_team,name='delete-team'),

]