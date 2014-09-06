# -*- coding: utf-8 -*-
from django.db import models

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
    anio = models.IntegerField(verbose_name='Año')
    division = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Curso')
        verbose_name_plural = ('Cursos')

    def __unicode__(self):
        return "%s, %s" % (self.anio, self.division)


class CursoMateria(models.Model):
    curso = models.ForeignKey('Curso')
    profesor = models.ForeignKey('Profesor')
    anio_materia = models.ForeignKey('AnioMateria')

    class Meta:
        verbose_name = ('CursoMateria')
        verbose_name_plural = ('CursoMateria')

    def __unicode__(self):
        return "%s, %s" % (self.anio, self.division)


class AnioMateria(models.Model):
    materia = models.ForeignKey('Materia')
    anio = models.IntegerField(verbose_name='Año')

    class Meta:
        verbose_name = ('AnioMateria')
        verbose_name_plural = ('AnioMateria')

    def __unicode__(self):
        return "%s, %s" % (self.anio, self.materia)


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    area_tematica = models.ForeignKey('AreaTematica')

    class Meta:
        verbose_name = ('AnioMateria')
        verbose_name_plural = ('AnioMateria')

    def __unicode__(self):
        return self.nombre


class AreaTematica(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Area Tematica')
        verbose_name_plural = ('Areas Tematicas')

    def __unicode__(self):
        return self.nombre


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
    adjunto = models.FileField(upload_to='recursos')
    area_tematica = models.ForeignKey('AreaTematica')
    anio = models.IntegerField(verbose_name='Año')

    class Meta:
        verbose_name = ('Eje')
        verbose_name_plural = ('Ejes')

    def __unicode__(self):
        return self.nombre
