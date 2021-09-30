from os import name
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.login_page,name='login'),
    path('Home',views.Home,name='home'),
    path('Profile',views.profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('register',views.register,name='register'),
    path('post',views.create_post,name='post'),
    path('update',views.update_profile,name='update')
]
