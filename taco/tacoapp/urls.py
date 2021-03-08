from django.contrib import admin
from django.urls import path
from tacoapp import views

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'tacoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('reset/', views.reset, name='reset')

    # path('manager/', views.manager, name='manager'),
    # path('details/', views.details, name='details'),
]
