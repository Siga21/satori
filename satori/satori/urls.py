"""satori URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from cafe import views
from cafe.views import ListaTareas, ListaLocales, DetalleLocales, ListaZonas, DetalleTareas
from cafe.forms import CrearTarea

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^locales/', ListaLocales.as_view(), name='ListaLocales'),
    url(r'^zonas/', ListaZonas.as_view(), name='ListaZonas'),
    url(r'^locales_detalle/(?P<pk>[0-9]+)/$', DetalleLocales.as_view(), name = 'Locales_Detalle'),
    url(r'^tareas/', ListaTareas.as_view(), name='ListaTareas'),
    url(r'^tareas_detalle/(?P<pk>[0-9]+)/$', DetalleTareas.as_view(), name = 'Tareas_Detalle'),
    url(r'^tareas_agregar/$', CrearTarea.as_view(), name='AgregarTarea'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
