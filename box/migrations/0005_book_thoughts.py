# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-31 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180513_1611'),
        ('box', '0004_auto_20180820_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thoughts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Entry', verbose_name='\u8bfb\u540e\u611f'),
        ),
    ]
