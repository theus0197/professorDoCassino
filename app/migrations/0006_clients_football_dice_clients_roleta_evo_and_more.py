# Generated by Django 4.2.3 on 2023-08-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_clients_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='football_dice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clients',
            name='roleta_evo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clients',
            name='roleta_playtec',
            field=models.BooleanField(default=False),
        ),
    ]