# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 00:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20161221_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
