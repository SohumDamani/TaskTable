# Generated by Django 4.0.6 on 2022-07-28 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Status',
            new_name='status',
        ),
    ]
