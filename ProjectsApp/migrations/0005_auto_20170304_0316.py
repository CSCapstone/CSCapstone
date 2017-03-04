# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-04 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0004_auto_20170204_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(to='ProjectsApp.ProgrammingLanguage'),
        ),
    ]
