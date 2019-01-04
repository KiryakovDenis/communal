from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('home', views.home, name='HomePage'),      
    #path('', views.home, name='HomePage'), 
    path('home/', views.home.as_view(), name='HomePage'),
    path('', views.home.as_view(), name='HomePage'),
]