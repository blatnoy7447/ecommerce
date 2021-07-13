from django.contrib import admin
from django.urls import path, include
from mainapp import views


urlpatterns = [
    path('admin/', views.adminLogin),
    path('', include('mainapp.urls')),
]
