# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-20 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0003_summary_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='\u6458\u8981\u5185\u5bb9HTML'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='page',
            field=models.CharField(blank=True, max_length=150, verbose_name='\u9875\u7801\u4fe1\u606f'),
        ),
    ]
