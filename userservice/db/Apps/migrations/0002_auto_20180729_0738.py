# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-29 07:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_table',
            name='deviec_id',
        ),
        migrations.AddField(
            model_name='login_table',
            name='device_id',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='login_table',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='login_table',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 7, 38, 55, 563922)),
        ),
        migrations.AlterField(
            model_name='login_table',
            name='logout_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='login_table',
            name='token',
            field=models.CharField(default=b'1f34838f-6b60-4eb6-b7a3-13b735a6cfd1', max_length=128),
        ),
    ]