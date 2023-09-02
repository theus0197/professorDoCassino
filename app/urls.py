from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test_iframe),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    #Old clients
    path('client/add', views.add_client, name='add_client'),
    path('add/newClient', views.add_new_client, name='add_new_client'),
    path('get/client', views.get_client, name='get_client'),
    path('view/client', views.view_client, name='view_client'),
    path('update/client', views.update_client, name='update_client'),
    path('delete/client', views.delete_client, name='delete_client'),
    path('api/v1/clients', views.api_get_clients, name='get_client'),
    path('api/v1/verify/game', views.api_get_game, name='get_game'),
]
