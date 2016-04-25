from django.contrib import admin

from cafe.models import zonas, locales, tipos_tareas, tareas, provincias

# Register your models here.

admin.site.register(zonas)
admin.site.register(locales)
admin.site.register(tipos_tareas)
admin.site.register(tareas)
admin.site.register(provincias)
