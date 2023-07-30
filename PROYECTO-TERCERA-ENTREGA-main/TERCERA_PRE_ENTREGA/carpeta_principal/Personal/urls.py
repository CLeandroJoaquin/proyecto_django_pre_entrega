from django.urls import include, path
from django.contrib import admin
from Personal import views
urlpatterns = [
    path("", views.lista_personal,name="Personal")
    
]