from django.urls import include, path
from django.contrib import admin
from Personal import views
urlpatterns = [
    path('Personal/', views.Personal)
    
]