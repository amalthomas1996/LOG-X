# Generated by Django 4.1 on 2024-03-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_rename_project_id_team_projectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.IntegerField(),
        ),
    ]
