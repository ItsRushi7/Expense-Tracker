from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('signup/', views.signup, name='Signup'),
    path('home/', views.Home, name='Home'),
    path('home/delete/<int:id>/', views.Delete, name='Delete'),
    path('home/edit/<int:id>/', views.Edit, name='Edit'),    
]
