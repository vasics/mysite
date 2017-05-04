# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 12:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0004_auto_20170426_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer04a',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer04q',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000, null=True)),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer04',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer04',
        ),
    ]