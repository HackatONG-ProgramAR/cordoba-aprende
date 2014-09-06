# -*- coding: utf-8 -*-
from django.db import models
from educar import get_descripciones_ebooks

# Create your models here.


class Alumno(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    colegio = models.ForeignKey('Colegio')
    curso = models.ForeignKey('Curso')
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = ('Alumno')
        verbose_name_plural = ('Alumnos')

    def __unicode__(self):
        return "%s, %s" % (self.apellido, self.nombre)


class Profesor(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    colegio = models.ForeignKey('Colegio')
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = ('Profesor')
        verbose_name_plural = ('Profesores')

    def __unicode__(self):
        return "%s, %s" % (self.apellido, self.nombre)


class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Colegio')
        verbose_name_plural = ('Colegios')

    def __unicode__(self):
        return self.nombre


class Curso(models.Model):
    colegio = models.ForeignKey('Colegio')
    anio = models.IntegerField(verbose_name=u'Año')
    division = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Curso')
        verbose_name_plural = ('Cursos')

    def __unicode__(self):
        return u'%s "%s"' % (self.anio, self.division)


class CursoMateria(models.Model):
    curso = models.ForeignKey('Curso')
    profesor = models.ForeignKey('Profesor')
    anio_materia = models.ForeignKey('AnioMateria')

    class Meta:
        verbose_name = ('Curso Materia')
        verbose_name_plural = ('Curso Materias')

    def __unicode__(self):
        return u"%s - %s - %s" % (self.curso, self.anio_materia, self.profesor)


class AnioMateria(models.Model):
    materia = models.ForeignKey('Materia')
    anio = models.IntegerField(verbose_name=u'Año')

    class Meta:
        verbose_name = (u'Año Materia')
        verbose_name_plural = (u'Año Materias')

    def __unicode__(self):
        return u"%s - %s" % (self.materia, self.anio)


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    area_tematica = models.ForeignKey('AreaTematica')

    class Meta:
        verbose_name = ('Materia')
        verbose_name_plural = ('Materias')

    def __unicode__(self):
        return self.nombre


class AreaTematica(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Área Temática')
        verbose_name_plural = ('Áreas Temáticas')

    def __unicode__(self):
        return self.nombre

    @classmethod
    def crear_areas(cls):
        areas = ["Matemática", "Lengua", "Ciencias"]
        for n in areas:
            cls.objects.create(nombre=n)


class Eje(models.Model):
    nombre = models.CharField(max_length=100)
    anio_materia = models.ForeignKey('AnioMateria')
    # contenidos

    class Meta:
        verbose_name = ('Eje')
        verbose_name_plural = ('Ejes')

    def __unicode__(self):
        return self.nombre


class Recurso(models.Model):
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace = models.TextField()
    adjunto = models.FileField(upload_to='recursos')
    area_tematica = models.ForeignKey('AreaTematica')
    anio = models.IntegerField(verbose_name=u'Año')

    class Meta:
        verbose_name = ('Recurso')
        verbose_name_plural = ('Recursos')

    @classmethod
    def cargar_ebooks(cls, descripciones=None):
        if descripciones is None:
            descripciones = get_descripciones_ebooks()
        # TODO: traer el area posta
        area = AreaTematica.objects.get(nombre="Ciencias")
        for desc in descripciones:
            cls.objects.create(
                    tipo="ebook",
                    nombre=desc[u'titulo'],
                    descripcion=desc['descripcion'],
                    area_tematica=area,
                    anio=3,
                    enlace=desc['visualizacion_educar']
                )

    def __unicode__(self):
        return self.nombre
