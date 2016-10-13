# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-13 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0005_meal_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_group', to='auth.Group'),
        ),
    ]
