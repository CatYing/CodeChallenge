# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccode', '0002_auto_20160516_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
