# Generated by Django 4.0.4 on 2022-10-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdiseases', '0016_alter_pesticides_crop_id_alter_pesticides_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='crop_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='crops',
            name='crop_year',
            field=models.BigIntegerField(),
        ),
    ]
