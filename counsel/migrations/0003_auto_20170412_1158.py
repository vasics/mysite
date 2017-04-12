# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsel', '0002_auto_20170410_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsel01',
            name='password',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='counsel01',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='%y/%m/%d'),
        ),
    ]