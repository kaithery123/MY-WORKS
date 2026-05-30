from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.login, name = 'login'),
    path('sign', views.signup, name = 'sign'),
    path('welcome', views.welcome, name = 'welcome'),
    path('logout', views.logout, name = 'logout'),
    

]
