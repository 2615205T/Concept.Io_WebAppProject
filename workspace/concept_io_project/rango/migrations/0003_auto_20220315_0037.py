# Generated by Django 2.2.26 on 2022-03-15 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20220314_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='dislikes'),
        ),
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
    ]