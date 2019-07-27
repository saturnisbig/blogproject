# Generated by Django 2.2.3 on 2019-07-27 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_auto_20180531_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='名称')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='组织名称')),
                ('link', models.URLField(blank=True, verbose_name='网站地址')),
                ('desc', models.TextField(blank=True, verbose_name='简介')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.Category', verbose_name='所属国家')),
            ],
            options={
                'ordering': ('-c_time',),
            },
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': '国家', 'verbose_name_plural': '国家'},
        ),
        migrations.RemoveField(
            model_name='country',
            name='level',
        ),
        migrations.RemoveField(
            model_name='country',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='country',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='country',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='country',
            name='tree_id',
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
        migrations.AddField(
            model_name='site',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.Country', verbose_name='所属国家'),
        ),
    ]
