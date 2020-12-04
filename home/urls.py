from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('result/' , views.result),
    path('theme/' , views.theme)
]
