# Generated by Django 4.2.1 on 2023-05-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_truck_currenct_lat_alter_truck_currenct_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='currenct_lat',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='truck',
            name='currenct_lng',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
