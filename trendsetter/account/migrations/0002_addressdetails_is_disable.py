# Generated by Django 4.1.7 on 2023-04-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressdetails',
            name='is_disable',
            field=models.BooleanField(default=False),
        ),
    ]
