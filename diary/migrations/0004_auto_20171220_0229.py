# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 02:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20171220_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 20, 2, 29, 43, 63432, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 20, 2, 29, 43, 63917, tzinfo=utc)),
        ),
    ]
