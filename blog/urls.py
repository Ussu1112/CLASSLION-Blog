from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/<int:blog_id>/', views.detail, name="detail"),
    path('list/', views.lists, name="list"),
    path('sellitem/', views.sellitem, name='sellitem'),
] 