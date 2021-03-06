# Generated by Django 3.0.7 on 2020-07-10 14:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('f', models.TextField(verbose_name='Фамилия')),
                ('i', models.TextField(verbose_name='Имя')),
                ('o', models.TextField(verbose_name='Отчество')),
                ('contractid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер договора')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 7, 10, 14, 5, 37, 835631, tzinfo=utc), verbose_name='Дата регистрации')),
                ('info', models.TextField(default='Info about user', verbose_name='Примечания')),
            ],
            options={
                'verbose_name': 'Пользователи',
            },
        ),
    ]
