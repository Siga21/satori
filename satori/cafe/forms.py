#encoding:utf-8

from django.forms import ModelForm
from django import forms
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render_to_response, get_object_or_404

from cafe.models import tareas, locales, zonas, provincias, tipos_tareas
#class clienteForm(ModelForm):
#	class Meta:
#		model = clientes
#		fields = "__all__"

class CrearTarea(CreateView):
    model = tareas
    fields = ['tarea', 'local', 'fecha', 'completada', 'observaciones',]
