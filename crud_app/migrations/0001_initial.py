# Generated by Django 4.1.6 on 2023-08-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=20)),
                ('s_email', models.CharField(max_length=30)),
                ('s_contact', models.CharField(max_length=10)),
            ],
        ),
    ]