# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fone2',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
