# Generated by Django 4.0.4 on 2022-10-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdiseases', '0005_pesticides_fertizer_for_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='farmland',
            field=models.IntegerField(),
        ),
    ]
