# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20170419_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer03',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer03',
            name='start_date',
            field=models.DateField(),
        ),
    ]
