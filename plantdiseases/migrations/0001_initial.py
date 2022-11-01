# Generated by Django 4.0.4 on 2022-10-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bacterialdiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('causative_agent', models.CharField(max_length=10000)),
                ('hosts', models.CharField(max_length=100)),
                ('symptoms', models.IntegerField()),
                ('pesticides', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='fungaldiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('causative_agent', models.CharField(max_length=10000)),
                ('hosts', models.CharField(max_length=100)),
                ('symptoms', models.IntegerField()),
                ('pesticides', models.CharField(max_length=1000)),
            ],
        ),
    ]