# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_auto_20181202_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbet',
            name='bet_status',
            field=models.CharField(choices=[('1', 'win'), ('X', 'pending'), ('0', 'lost')], default='X', max_length=1),
        ),
    ]