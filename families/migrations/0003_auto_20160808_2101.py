# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0002_auto_20160808_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='group',
            new_name='family_group',
        ),
    ]
