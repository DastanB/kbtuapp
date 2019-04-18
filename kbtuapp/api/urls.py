from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.InfoList.as_view()),
    path('info/<int:pk>/', views.InfoDetails.as_view()),
    path('photo/', views.PhotoList.as_view()),
    path('photo/<int:pk>/', views.PhotoDetails.as_view())   
]