# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0005_auto_20161203_2124'),
        ('GroupsApp', '0005_auto_20161204_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='project',
        ),
        migrations.AddField(
            model_name='group',
            name='project',
            field=models.ManyToManyField(default=None, null=True, to='ProjectsApp.Project'),
        ),
    ]
