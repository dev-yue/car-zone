# Generated by Django 3.0.7 on 2023-01-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20230108_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(max_length=100),
        ),
    ]
