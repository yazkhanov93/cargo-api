# Generated by Django 4.2.1 on 2023-05-27 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('post_code_zip', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('currenct_lat', models.FloatField()),
                ('currenct_lng', models.FloatField()),
                ('load_capacity', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Trucks',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('description', models.TextField()),
                ('location_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_delivery', to='store.location')),
                ('location_pick_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_pick_up', to='store.location')),
            ],
            options={
                'verbose_name_plural': 'Cargos',
            },
        ),
    ]
