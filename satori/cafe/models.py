from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class zonas(models.Model):
	zona = models.CharField(max_length=50)

	def __unicode__(self):
		return self.zona

class locales(models.Model):
    local = models.CharField(max_length=75)
	telefono = models.CharField(max_lenght=15)
	movil = models.CharField(max_length=15)
    correo = models.EmailField()
    contacto = models.CharFields(max_length=75)
	direccion = models.CharField(max_length=100)
	codigo_postal = models.CharField(max_length=7)
	poblacion = models.CharField(max_length=100)
	provincia = models.CharField(max_length=100)
	zona = models.ForeignKey(zonas, default=None, null=True, blank=True)
	maquina = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
    centralita = models.CharField(max_length=100)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=True)
	fecha_ultima = models.DateTimeField(default=datetime.now, blank=True)
    es_siga = models.BooleanField(null=True, blank=True)
	observaciones = models.TextField(default=None, null=True)

    def __unicode__(self):
    	return self.local

class tipos_tareas(models.Model):
	tipo = models.CharField(max_length=75)

	def __unicode__(self):
		return self.tipo


class tareas(models.Model):
	tarea = models.ForeignKey(tipos_tareas, default=None, null=True, blank=True)
	local = models.ForeignKey(locales, default=None, null=True, blank=True)
	fecha = models.DateTimeField(default=datetiem.now, blank=True)
	completada = models.booleanField(null=True, blank=True)
    observaciones = models.TextField(default=None, null=True)

    def __unicode__(self):
    	return self.tarea
