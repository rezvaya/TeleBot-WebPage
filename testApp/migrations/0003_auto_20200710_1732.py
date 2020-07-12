# Generated by Django 3.0.7 on 2020-07-10 14:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20200710_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Личный счет', 'verbose_name_plural': 'Личный счет'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователи', 'verbose_name_plural': 'Личный счет'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='contractid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='testApp.Users', verbose_name='Номер договора'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_trans',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 14, 32, 44, 611009, tzinfo=utc), verbose_name='Дата последнего платежа'),
        ),
        migrations.AlterField(
            model_name='users',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 14, 32, 44, 611009, tzinfo=utc), verbose_name='Дата регистрации'),
        ),
    ]
