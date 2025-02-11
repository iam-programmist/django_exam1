# Generated by Django 5.0 on 2024-10-22 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=3, unique=True)),
                ('currency_name', models.CharField(max_length=50)),
                ('symbol', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=6, max_digits=15)),
                ('date', models.DateField()),
                ('base_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_currency_rates', to='exchange_rate.currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_currency_rates', to='exchange_rate.currency')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_rate', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True)),
                ('new_rate', models.DecimalField(decimal_places=6, max_digits=15)),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('base_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_currency_history', to='exchange_rate.currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_currency_history', to='exchange_rate.currency')),
            ],
        ),
    ]
