# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-15 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0005_auto_20161015_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='electric-forest', editable=False, max_length=60),
            preserve_default=False,
        ),
    ]
