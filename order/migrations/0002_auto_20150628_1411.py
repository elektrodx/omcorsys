# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivered',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_due',
            field=models.DateField(null=True, blank=True),
        ),
    ]
