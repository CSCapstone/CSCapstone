# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0003_auto_20170204_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(default=b'', max_length=10000),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
