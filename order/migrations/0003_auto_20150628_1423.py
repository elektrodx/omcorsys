# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150628_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='invoice',
            field=models.ForeignKey(blank=True, to='order.Invoice', null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
