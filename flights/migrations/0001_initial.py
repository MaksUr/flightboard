# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-19 05:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import flights.validators
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Авиакомпания')),
                ('code', models.CharField(max_length=2, validators=[flights.validators.airline_code_validate], verbose_name='Код авиакомпании')),
            ],
            options={
                'verbose_name': 'Авиалиния',
                'verbose_name_plural': 'Авиалинии',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название аэропорта')),
                ('code', models.CharField(max_length=3, validators=[flights.validators.airport_code_validate], verbose_name='Код аэропорта')),
            ],
            options={
                'verbose_name': 'Aэропорт',
                'verbose_name_plural': 'Aэропорты',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название города')),
                ('country_code', models.CharField(max_length=3, validators=[flights.validators.country_code_validate], verbose_name='Код страны')),
                ('timezone', timezone_field.fields.TimeZoneField(verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[flights.validators.flight_number_validate], verbose_name='Номер рейса')),
                ('duration', models.DurationField(verbose_name='В пути')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Airline', verbose_name='Авиалиния')),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_arr', to='flights.Airport', verbose_name='Аэропорт прибытия')),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_dep', to='flights.Airport', verbose_name='Аэропорт вылета')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
        migrations.CreateModel(
            name='ScheduleFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_departure', models.DateTimeField(verbose_name='Время вылета.')),
                ('time_of_arrival', models.DateTimeField(verbose_name='Фактическое местное время прибытия.')),
                ('status', models.CharField(choices=[('flying', 'В полете'), ('arrive', 'Прибыл'), ('registration', 'Регистрация')], max_length=20, verbose_name='Статус рейса.')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight', verbose_name='Рейс')),
            ],
            options={
                'verbose_name': 'Фактический рейс',
                'verbose_name_plural': 'Фактические рейсы',
            },
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.City', verbose_name='Город'),
        ),
    ]
