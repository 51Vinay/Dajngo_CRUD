# Generated by Django 4.1.6 on 2023-08-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_id',
            new_name='id',
        ),
    ]