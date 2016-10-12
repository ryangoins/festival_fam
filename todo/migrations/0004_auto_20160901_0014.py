# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_assignee_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_items_list', to='todo.List'),
        ),
    ]