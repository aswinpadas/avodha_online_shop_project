# Generated by Django 4.0.4 on 2022-06-23 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_product_id_cartmodel_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartmodel',
            name='product_qty',
        ),
    ]
