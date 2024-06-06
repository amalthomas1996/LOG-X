# Generated by Django 4.1 on 2024-02-26 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='team_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Admin.team'),
            preserve_default=False,
        ),
    ]
