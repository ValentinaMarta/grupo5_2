from django.contrib import admin
from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', login, name="iniciar"),
    path('inicio/', inicio, name="home"),
    path('registro/', registro, name="registrar"),
    path('contraseña/', contraseña),
    path('recuperada/', recuperada),
    path('lecciones/', lecciones, name="leccion"),
    path('calificaciones/', calificaciones, name="notas"),
    path('alumnos/', alumnos, name="alumno"),
    path('alumnos/nuevoalumno/', alumnoNuevo, name="nuevoAlumno"),
    path('alumnos/editar/<int:id>', editarAlumno),
    path('alumnos/eliminaralumno/<int:id>', eliminarAlumno),
    path('anadirLeccion/', anadirLeccion, name="anadirLeccion"),

]
