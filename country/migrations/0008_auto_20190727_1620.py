# Generated by Django 2.2.3 on 2019-07-27 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0007_auto_20190727_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ('-c_time',), 'verbose_name': '网站信息', 'verbose_name_plural': '网站信息'},
        ),
    ]
