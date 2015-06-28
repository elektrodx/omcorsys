# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_ci'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guia', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('date_arrive', models.DateField(blank=True)),
                ('amount', models.DecimalField(max_digits=7, decimal_places=2)),
                ('amount_tax', models.DecimalField(max_digits=7, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('source', models.URLField()),
                ('code', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True)),
                ('weight', models.DecimalField(max_digits=7, decimal_places=2, blank=True)),
                ('tracking', models.URLField(max_length=500, blank=True)),
                ('note', models.TextField()),
                ('invoice', models.ForeignKey(to='order.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_due', models.DateField(blank=True)),
                ('date_delivered', models.DateField(blank=True)),
                ('amount', models.DecimalField(max_digits=7, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=7, decimal_places=2)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.ForeignKey(to='order.State'),
        ),
        migrations.AddField(
            model_name='items',
            name='order',
            field=models.ForeignKey(to='order.Order'),
        ),
    ]
