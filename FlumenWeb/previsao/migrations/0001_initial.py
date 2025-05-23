# Generated by Django 4.2.11 on 2025-05-14 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Previsao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora', models.DateTimeField()),
                ('data_hora_inicio', models.DateTimeField()),
                ('data_hora_final', models.DateTimeField()),
                ('temperatura_max', models.FloatField()),
                ('temperatura_min', models.FloatField()),
                ('luminosidade', models.FloatField()),
                ('chuva', models.FloatField()),
                ('umidade_ar', models.FloatField()),
                ('umidade_solo', models.FloatField()),
                ('qualidade_ar', models.FloatField()),
                ('PrevisaoCol', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('Estacao_idEstacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacao.estacao')),
            ],
            options={
                'db_table': 'flu_previsao',
            },
        ),
    ]
