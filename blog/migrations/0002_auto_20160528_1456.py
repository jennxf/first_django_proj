# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 21:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 21, 56, 26, 459849, tzinfo=utc)),
        ),
    ]
