# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('flavor', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('sugar_mg', models.FloatField()),
                ('price_dollars', models.PositiveSmallIntegerField()),
                ('has_topping', models.BooleanField(default=False)),
            ],
        ),
    ]
