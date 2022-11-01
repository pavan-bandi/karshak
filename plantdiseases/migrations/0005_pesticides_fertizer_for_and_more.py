# Generated by Django 4.0.4 on 2022-10-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdiseases', '0004_crops_rename_adhaarno_farmer_farmerid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesticides',
            name='fertizer_for',
            field=models.CharField(default=12, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pesticides',
            name='fert_or_pest',
            field=models.CharField(max_length=100),
        ),
    ]