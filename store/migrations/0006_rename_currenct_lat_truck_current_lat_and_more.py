# Generated by Django 4.2.1 on 2023-05-29 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_truck_currenct_lat_alter_truck_currenct_lng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck',
            old_name='currenct_lat',
            new_name='current_lat',
        ),
        migrations.RenameField(
            model_name='truck',
            old_name='currenct_lng',
            new_name='current_lng',
        ),
    ]