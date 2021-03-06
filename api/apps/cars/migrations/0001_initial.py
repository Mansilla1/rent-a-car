# Generated by Django 2.2.4 on 2020-05-17 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='nombre', max_length=255)),
            ],
            options={
                'db_table': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('doors', models.IntegerField(db_column='puertas')),
                ('high', models.DecimalField(db_column='alto', decimal_places=2, max_digits=5, null=True)),
                ('long', models.DecimalField(db_column='largo', decimal_places=2, max_digits=5, null=True)),
                ('width', models.DecimalField(db_column='ancho', decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(db_column='peso', decimal_places=2, max_digits=5, null=True)),
                ('diesel', models.BooleanField()),
                ('description', models.TextField(db_column='descripcion', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'autos',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='nombre', max_length=255)),
                ('brand', models.ForeignKey(db_column='marca', on_delete=django.db.models.deletion.DO_NOTHING, related_name='brand', to='cars.Brand')),
            ],
            options={
                'db_table': 'modelos',
            },
        ),
        migrations.CreateModel(
            name='CarAvailability',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_column='disponible', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(db_column='auto', on_delete=django.db.models.deletion.CASCADE, related_name='car', to='cars.Car')),
            ],
            options={
                'db_table': 'disponibilidad_auto',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(db_column='modelo', on_delete=django.db.models.deletion.DO_NOTHING, related_name='model', to='cars.Model'),
        ),
    ]
