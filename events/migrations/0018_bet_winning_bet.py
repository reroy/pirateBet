# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20181122_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='winning_bet',
            field=models.BooleanField(default=False),
        ),
    ]
