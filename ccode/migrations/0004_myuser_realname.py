# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-17 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccode', '0003_auto_20160516_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='realname',
            field=models.CharField(default='defalut', max_length=256),
            preserve_default=False,
        ),
    ]
