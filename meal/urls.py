from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('meal/', views.item, name='item'),

]
