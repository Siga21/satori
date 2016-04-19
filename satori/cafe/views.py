from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import datetime, timedelta
from django.utils import timezone
from cafe.models import zonas, locales, tipos_tareas, tareas
# Create your views here.

class ListaTareas(ListView):
    initime = datetime.strptime('0000','%H%M').time()
    fintime = datetime.strptime('2359','%H%M').time()
    principio = datetime.combine(datetime.today(), initime)
    fin = datetime.combine(datetime.today(), fintime)
    queryset = tareas.objects.filter(fecha__gte = principio, fecha__lte = fin, completada = False).order_by('fecha')
    context_object_name = 'tareas'
    paginate_by = 8

class ListaLocales(ListView):
    queryset = locales.objects.order_by('local')
    context_object_name = 'locales'
    paginate_by = 8
    
class DetalleLocales(DetailView):
    model = locales

class ListaZonas(ListView):
	queryset = zonas.objects.order_by('id')
	context_object_name = 'zonas'
	paginate_by = 8

class ListaDeTareas(ListView):
	queryset = tareas.objects.order_by('-fecha')
	context_object_name = 'tareas'
	paginated_by = 8


