# Generated by Django 4.2.11 on 2025-04-02 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacao', '0002_alter_estacao_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacao',
            old_name='idEstacao',
            new_name='id',
        ),
    ]
