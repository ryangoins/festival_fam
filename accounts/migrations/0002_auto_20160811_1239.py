# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userName',
            new_name='user',
        ),
    ]