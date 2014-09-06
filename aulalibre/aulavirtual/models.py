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
