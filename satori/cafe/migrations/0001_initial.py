# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 11:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=75)),
                ('telefono', models.CharField(max_length=15)),
                ('movil', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('contacto', models.CharField(max_length=75)),
                ('direccion', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=7)),
                ('poblacion', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('maquina', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('centralita', models.CharField(max_length=100)),
                ('fecha_alta', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_ultima', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('es_siga', models.BooleanField()),
                ('observaciones', models.TextField(default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'locales',
            },
        ),
        migrations.CreateModel(
            name='tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('completada', models.BooleanField()),
                ('observaciones', models.TextField(default=None, null=True)),
                ('local', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cafe.locales')),
            ],
            options={
                'verbose_name_plural': 'tareas',
            },
        ),
        migrations.CreateModel(
            name='tipos_tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name_plural': 'tipos_tareas',
            },
        ),
        migrations.CreateModel(
            name='zonas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'zonas',
            },
        ),
        migrations.AddField(
            model_name='tareas',
            name='tarea',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cafe.tipos_tareas'),
        ),
        migrations.AddField(
            model_name='locales',
            name='zona',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cafe.zonas'),
        ),
    ]
