# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0005_auto_20161129_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
