# Generated by Django 4.0.4 on 2022-10-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdiseases', '0010_alter_pesticides_crop_id_alter_pesticides_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesticides',
            name='crop_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pesticides',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
