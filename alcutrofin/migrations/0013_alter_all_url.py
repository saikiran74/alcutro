# Generated by Django 3.2 on 2021-12-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcutrofin', '0012_all_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
