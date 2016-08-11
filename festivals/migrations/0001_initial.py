# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, default='', upload_to='')),
                ('twitter', models.URLField(blank=True, default='')),
                ('facebook', models.URLField(blank=True, default='')),
                ('snapchat', models.URLField(blank=True, default='')),
                ('faq_site', models.URLField(blank=True, default='')),
                ('homepage', models.URLField(blank=True, default='')),
                ('registration_site', models.URLField()),
            ],
        ),
    ]
