# Generated by Django 5.1.4 on 2024-12-30 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data_fotografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('Nebula', 'NEBULOSA'), ('Star', 'ESTRELA'), ('Galaxy', 'GALÁXIA'), ('PLANETA', 'Planet')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
