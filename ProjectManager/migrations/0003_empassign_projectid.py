# Generated by Django 4.1 on 2024-02-28 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_rename_project_id_team_projectid'),
        ('ProjectManager', '0002_empassign'),
    ]

    operations = [
        migrations.AddField(
            model_name='empassign',
            name='projectid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Admin.project'),
        ),
    ]
