# Generated by Django 3.2 on 2021-12-30 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alcutrofin', '0007_auto_20211230_2154'),
    ]

    operations = [
        migrations.DeleteModel(
            name='favourite',
        ),
        migrations.AddField(
            model_name='all',
            name='favourite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
