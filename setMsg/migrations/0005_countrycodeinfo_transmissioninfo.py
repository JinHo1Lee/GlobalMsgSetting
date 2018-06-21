# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setMsg', '0004_auto_20180619_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countrycodeinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.TextField(blank=True, null=True)),
                ('country_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'setMsg_countrycodeinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transmissioninfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission_name', models.TextField(blank=True, null=True)),
                ('tsg_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'setMsg_transmissioninfo',
                'managed': False,
            },
        ),
    ]