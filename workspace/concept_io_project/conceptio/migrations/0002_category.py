# Generated by Django 3.2.10 on 2022-03-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conceptio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
    ]
