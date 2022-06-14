from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('group/add', views.add_group, name='add_group'),
    path('group/new/add', views.add_new_group, name='add_group'),
    path('group/get', views.get_group, name='get_group'),
    path('group/view', views.view_group, name='view_group'),
    path('group/update', views.update_group, name='update_group'),
    path('group/delete', views.delete_group, name='delete_group'),
    path('api/groups', views.api_get_groups, name='get_groups'),
]
