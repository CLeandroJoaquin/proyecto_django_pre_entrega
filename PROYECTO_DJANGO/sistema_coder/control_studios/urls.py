#URLS específicas de LA APP

from django.contrib import admin
from django.urls import path
#Son las URLS generales del PROYECTO
from control_studios.views import (listar_estudiantes, listar_cursos, listar_cursos, crear_cursos, eliminar_curso, editar_curso, EstudianteListView,EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView, EstudianteDetailView)


urlpatterns= [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_cursos, name="crear_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
#basado en vistas
   path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
   path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
   path('crear-estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
   path('editar-estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
   path('eliminar-estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),


]

#eliminar-curso/100/
#id = 100