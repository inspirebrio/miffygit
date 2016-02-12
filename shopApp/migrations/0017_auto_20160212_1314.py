# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0016_auto_20160212_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_status',
            field=models.BooleanField(default=True, verbose_name=b'*ad_status', choices=[(True, b'Live'), (False, b'Pause')]),
            preserve_default=True,
        ),
    ]
