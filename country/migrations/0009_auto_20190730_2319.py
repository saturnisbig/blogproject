# Generated by Django 2.2.3 on 2019-07-30 15:19

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
# from mptt import register, managers
# def rebuild_tree(apps, schema_editor):
#     YourMPTTModel = apps.get_model('country', 'Country')

#     manager = managers.TreeManager()
#     manager.model = Country

#     register(Country)

#     manager.contribute_to_class(Country, 'objects')
#     manager.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0008_auto_20190727_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='country.Country'),
        ),
        migrations.AddField(
            model_name='country',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        # migrations.RunPython(
        #     rebuild_tree
        # ),
    ]