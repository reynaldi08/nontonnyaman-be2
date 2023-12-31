# Generated by Django 4.1.1 on 2023-10-04 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=40)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('is_staff', models.BooleanField(default=False)),
                ('role_users', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
