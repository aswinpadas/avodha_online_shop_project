# Generated by Django 4.0.4 on 2022-06-17 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UsersDB',
        ),
    ]