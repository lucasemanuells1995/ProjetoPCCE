# Generated by Django 4.0.4 on 2022-05-11 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Almoxarifado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternativa',
            old_name='texto_perguntas',
            new_name='texto_alternativa',
        ),
    ]