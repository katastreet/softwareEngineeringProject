# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20170206_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='officedata',
            name='canBeBought',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='officedata',
            name='leasable',
            field=models.BooleanField(default=False),
        ),
    ]
