# Generated by Django 4.0.6 on 2022-07-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_task_end_date_alter_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
