# Generated by Django 4.2.3 on 2023-08-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_clients_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]