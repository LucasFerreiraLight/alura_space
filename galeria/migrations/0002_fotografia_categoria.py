# Generated by Django 5.1.4 on 2024-12-27 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebula'), ('Star', 'ESTRELA'), ('Galaxy', 'GALÁXIA'), ('PLANETA', 'Planet')], default='', max_length=100),
        ),
    ]