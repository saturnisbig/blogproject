# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-13 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-c_time']},
        ),
        migrations.AlterField(
            model_name='entry',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
