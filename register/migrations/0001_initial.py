# Generated by Django 5.0.1 on 2024-01-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bemor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=40)),
                ('manzil', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Yollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('narx', models.PositiveIntegerField()),
                ('qayerga', models.CharField(max_length=50)),
            ],
        ),
    ]
