# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-11 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_bet_bet_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbet',
            name='factor',
            field=models.FloatField(default=1),
        ),
    ]
