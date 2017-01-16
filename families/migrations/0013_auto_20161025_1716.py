# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-25 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0012_auto_20161025_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
