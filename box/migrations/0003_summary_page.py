# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-05 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_auto_20180612_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='page',
            field=models.TextField(blank=True, verbose_name='\u9875\u7801\u4fe1\u606f'),
        ),
    ]
