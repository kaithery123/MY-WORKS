from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.login, name = 'login'),
    path('sign', views.signup, name = 'sign'),
    
    path('logout', views.logout, name = 'logout'),
    path('todo', views.todo, name = 'todo'),
    path('logout', views.logout, name = 'logout'),
    path('delete/(?P<a>\d+)', views.delete, name = 'delete'),
    path('update/(?P<b>\d+)', views.update, name = 'update'),
]