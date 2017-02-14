# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('modelNo', models.CharField(max_length=20)),
                ('modelDate', models.DateField(verbose_name='model date')),
                ('boughtdate', models.DateTimeField(verbose_name='boughtdate')),
                ('warrantyTimeInMonth', models.IntegerField(default=0)),
                ('boughtprice', models.FloatField(default=0)),
                ('depreciationRate', models.FloatField(default=0)),
                ('warantyAgentName', models.CharField(max_length=200)),
                ('warantyAgentLocation', models.CharField(max_length=200)),
                ('WarantyAgentPhoneNumber', models.CharField(max_length=25)),
                ('previousEvaluationDate', models.DateField(verbose_name='previously evaluated on')),
                ('toBeEvaluatedEveryMonth', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
