# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counsel01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('fp', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='%y/%m/%d')),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Counsel02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=15)),
                ('birth', models.CharField(max_length=20)),
                ('tel', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=10, null=True)),
                ('starttime', models.CharField(max_length=20, null=True)),
                ('endtime', models.CharField(max_length=20, null=True)),
                ('fp', models.CharField(max_length=15, null=True)),
                ('content', models.CharField(max_length=50, null=True)),
                ('agree', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
