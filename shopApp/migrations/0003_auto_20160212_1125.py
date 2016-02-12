# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_auto_20160212_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url1',
            field=models.URLField(max_length=800, verbose_name=b'*ad_url1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url2',
            field=models.URLField(max_length=800, verbose_name=b'*ad_url2'),
            preserve_default=True,
        ),
    ]
