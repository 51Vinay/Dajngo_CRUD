# Generated by Django 4.1.6 on 2023-08-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_rename_s_id_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_name',
            new_name='name',
        ),
    ]
