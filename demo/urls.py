from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.account,name='account'),
    path('dashboard',views.dashboard ,name='dashboard'),
    path('register',views.register,name='register'),
    path('lockscreen',views.lockscreen,name='lockscreen'),
    path('restaurant',views.restaurant,name='restaurant'),
]