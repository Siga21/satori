# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_zonas_provincia'),
    ]

    operations = [
        migrations.CreateModel(
            name='provincias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(blank=True, null=True)),
                ('provincia', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'provincias',
            },
        ),
    ]
