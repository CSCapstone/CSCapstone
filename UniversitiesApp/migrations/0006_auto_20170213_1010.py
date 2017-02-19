# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UniversitiesApp', '0005_auto_20170117_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='university',
            name='description',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='university',
            name='website',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
