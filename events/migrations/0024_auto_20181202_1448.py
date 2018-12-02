# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20181202_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbet',
            name='bet_status',
            field=models.CharField(choices=[('1', 'win'), ('X', 'pending'), ('0', 'lost')], default='pending', max_length=1),
        ),
        migrations.AlterField(
            model_name='bet',
            name='money_bet',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='userbet',
            name='money_bet',
            field=models.FloatField(default=0),
        ),
    ]