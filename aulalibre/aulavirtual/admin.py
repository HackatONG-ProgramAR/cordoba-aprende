from django.contrib import admin

from aulavirtual.models import (
    Alumno, Profesor, Colegio, Curso, CursoMateria,
    AnioMateria, Materia, AreaTematica, Eje, Recurso)

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Colegio)
admin.site.register(Curso)
admin.site.register(CursoMateria)
admin.site.register(AnioMateria)
admin.site.register(Materia)
admin.site.register(AreaTematica)
admin.site.register(Eje)
admin.site.register(Recurso)
