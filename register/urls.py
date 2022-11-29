from django.contrib import admin
from django.urls import path,include

from display import settings
from django.conf.urls.static import static

from register import views

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
]