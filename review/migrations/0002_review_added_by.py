# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-26 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='added_by',
            field=models.CharField(default='Emma', max_length=20),
        ),
    ]