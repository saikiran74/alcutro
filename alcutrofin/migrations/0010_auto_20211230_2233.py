# Generated by Django 3.2 on 2021-12-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcutrofin', '0009_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
        migrations.RemoveField(
            model_name='all',
            name='favourite',
        ),
        migrations.AddField(
            model_name='profile',
            name='favourite',
            field=models.ManyToManyField(related_name='Favourite', to='alcutrofin.All'),
        ),
    ]