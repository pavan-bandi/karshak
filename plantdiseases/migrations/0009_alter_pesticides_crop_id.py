# Generated by Django 4.0.4 on 2022-10-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdiseases', '0008_alter_pesticides_crop_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesticides',
            name='crop_id',
            field=models.IntegerField(default=0),
        ),
    ]