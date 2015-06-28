# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20150628_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ci',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
