from django.contrib import admin

from aulavirtual.models import (
    Alumno, Profesor, Colegio, Curso, CursoMateria,
    AnioMateria, Materia, AreaTematica, Eje, Recurso)

# Register your models here.


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'curso']
    search_fields = ('nombre', 'apellido')
    list_filter = ['curso', ]


class AnioMateriaAdmin(admin.ModelAdmin):
    list_display = ['materia', 'anio']
    search_fields = ('materia', )
    list_filter = ['materia', 'anio']


class ColegioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad']
    search_fields = ['nombre', 'ciudad']
    list_filter = ['ciudad']


class CursoMateriaAdmin(admin.ModelAdmin):
    list_display = ['anio_materia', 'profesor', 'curso']
    search_fields = ['anio_materia', 'profesor', 'curso']
    list_filter = ['anio_materia', 'profesor', 'curso']


class MateriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'area_tematica']
    search_fields = ['nombre', ]
    list_filter = ['area_tematica', ]


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'email', 'colegio']
    search_fields = ['apellido', 'nombre', 'email']
    list_filter = ['colegio', ]


class CursoAdmin(admin.ModelAdmin):
    list_display = ['anio', 'division', 'colegio']
    search_fields = ['colegio']
    list_filter = ['anio', 'division', 'colegio']


class EjeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'anio_materia']
    search_fields = ['nombre']
    list_filter = ['anio_materia', ]


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Colegio, ColegioAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(CursoMateria, CursoMateriaAdmin)
admin.site.register(AnioMateria, AnioMateriaAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(AreaTematica)
admin.site.register(Eje, EjeAdmin)
admin.site.register(Recurso)
