# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]