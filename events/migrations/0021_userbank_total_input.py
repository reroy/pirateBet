# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-25 17:14
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_userbet_bet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbank',
            name='total_input',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8),
        ),
    ]
