# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 02:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20171220_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 20, 2, 28, 30, 520357, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 20, 2, 28, 30, 520827, tzinfo=utc)),
        ),
    ]