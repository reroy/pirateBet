# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-11 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_userbank_user_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_type', models.CharField(choices=[('1', 'first'), ('X', 'draw'), ('2', 'second')], max_length=1)),
                ('money_bet', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.UserBank')),
            ],
        ),
    ]