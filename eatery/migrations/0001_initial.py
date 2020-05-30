# Generated by Django 3.0.3 on 2020-05-30 23:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('dateTimeCreated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('fistname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('dateTimeCreated', models.DateTimeField(max_length=30)),
                ('amountOutstanding', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='MenuTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('dateTimeCreated', models.DateTimeField(default=datetime.datetime(2020, 5, 31, 0, 11, 18, 446185), verbose_name='date created')),
                ('vendorid', models.IntegerField()),
                ('isRecurring', models.CharField(max_length=10)),
                ('frequencyOfReocurrance', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MessageStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='VendorTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('businessName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('dateTimeCreated', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Vendor',
            },
        ),
        migrations.CreateModel(
            name='OrderTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('customerid', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField()),
                ('amountDue', models.FloatField()),
                ('amountPaid', models.FloatField()),
                ('amountOutstanding', models.FloatField()),
                ('dateAndTimeOfOrder', models.DateField()),
                ('itemsOrdered', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='eatery.MenuTable')),
                ('orderStatus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='eatery.OrderStatus')),
                ('vendorid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='eatery.VendorTable')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=30)),
                ('subjectuser', models.CharField(max_length=30)),
                ('dateTimeCreated', models.DateTimeField(default=datetime.datetime(2020, 5, 31, 0, 11, 18, 453185), verbose_name='date sent')),
                ('message', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='eatery.OrderTable')),
                ('messageStatus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='eatery.MessageStatus')),
                ('orderid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='eatery.CustomerTable')),
            ],
        ),
    ]
