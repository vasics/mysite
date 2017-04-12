# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer03'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer04',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]