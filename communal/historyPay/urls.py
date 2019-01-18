from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [    
    path('PayList/', views.PayList.as_view(), name='PayList'),
    path('PeriodList/', views.PeriodList.as_view(), name='PeriodList'),
    path('serviceProviderList/', views.serviceProviderList.as_view(), name='serviceProviderList'),
    path('home/', views.home.as_view(), name='HomePage'),
    path('', views.home.as_view(), name='HomePage'),
]