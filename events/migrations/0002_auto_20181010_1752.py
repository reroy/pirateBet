# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='first_team',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='second_team',
            field=models.CharField(max_length=255),
        ),
    ]
