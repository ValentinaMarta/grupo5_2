from django.contrib import admin

# Register your models here.
from webapp.models import *


admin.site.register(Profesor)
admin.site.register(Lecciones)
admin.site.register(Alumnos)
admin.site.register(Calificaciones)

