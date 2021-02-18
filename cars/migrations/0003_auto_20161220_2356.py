# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 23:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0002_auto_20161220_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='drivers',
        ),
        migrations.AddField(
            model_name='car',
            name='first_owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
