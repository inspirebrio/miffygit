# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0022_auto_20160212_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url1',
            field=models.URLField(default=0, max_length=800, verbose_name=b'*ad_url1', blank=True),
            preserve_default=False,
        ),
    ]
