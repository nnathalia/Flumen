# Generated by Django 4.2.11 on 2025-04-02 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('previsao', '0002_alter_previsao_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='previsao',
            old_name='idPrevisao',
            new_name='id',
        ),
    ]
