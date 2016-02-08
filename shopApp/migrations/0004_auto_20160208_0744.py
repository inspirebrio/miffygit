# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_auto_20160208_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(default=True, max_length=800, choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
    ]
