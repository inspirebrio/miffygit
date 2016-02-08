# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_auto_20160208_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(default=True, max_length=800, choices=[(0, b'text'), (1, b'image')]),
            preserve_default=True,
        ),
    ]
