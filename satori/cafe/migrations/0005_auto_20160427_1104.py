# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_provincias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locales',
            name='provincia',
        ),
        migrations.AlterField(
            model_name='zonas',
            name='provincia',
            field=models.ForeignKey(blank=True, default='Pontevedra', null=True, on_delete=django.db.models.deletion.CASCADE, to='cafe.provincias'),
        ),
    ]
