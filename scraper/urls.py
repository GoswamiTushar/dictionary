from django.contrib import admin
from django.urls import path, include
from scraper import views

urlpatterns = [
    path('', views.parse_info, name='parse_info'),
]
