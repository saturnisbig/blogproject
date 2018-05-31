# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-27 12:10
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_auto_20180526_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='country.Country', verbose_name='\u4e0a\u4e00\u7ea7'),
        ),
    ]