# Generated by Django 4.1.12 on 2023-10-24 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='reading date')),
                ('reading_period', models.CharField(max_length=100, verbose_name='reading period')),
                ('hot_water_reading', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='hot water reading')),
                ('cold_water_reading', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='cold water reading')),
                ('gas_reading', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='gas reading')),
                ('electricity_reading', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='electricity reading')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'meter reading',
                'verbose_name_plural': 'meter readings',
            },
        ),
    ]
