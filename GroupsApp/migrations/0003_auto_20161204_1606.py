# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0002_group_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProjectsApp.Project'),
        ),
    ]
