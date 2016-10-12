# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 17:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('families', '0008_auto_20160914_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_location_name', models.CharField(blank=True, default='', max_length=255)),
                ('departure_street', models.CharField(blank=True, default='', max_length=255)),
                ('departure_city', models.CharField(blank=True, default='', max_length=255)),
                ('departure_state', models.CharField(blank=True, default='', max_length=2)),
                ('departure_zip', models.IntegerField(blank=True, default='')),
                ('parking_pass', models.BooleanField(default=False)),
                ('driver', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_driver', to=settings.AUTH_USER_MODEL)),
                ('group', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_group', to='auth.Group')),
                ('passengers', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_passengers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]