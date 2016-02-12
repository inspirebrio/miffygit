# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0014_auto_20160212_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_status',
            field=models.BooleanField(default=True, choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
    ]
