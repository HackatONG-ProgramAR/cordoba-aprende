from django.contrib import admin

from aulavirtual.models import Alumno, Profesor, Colegio, Curso

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Colegio)
admin.site.register(Curso)

