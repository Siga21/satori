# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_auto_20160427_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zonas',
            name='provincia',
            field=models.ForeignKey(blank=True, default='36', null=True, on_delete=django.db.models.deletion.CASCADE, to='cafe.provincias'),
        ),
    ]