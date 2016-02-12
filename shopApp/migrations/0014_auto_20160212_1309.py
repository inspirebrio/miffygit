# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0013_auto_20160212_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_status',
            field=models.BooleanField(default=True, choices=[(True, b'Live'), (False, b'Pause')]),
            preserve_default=True,
        ),
    ]
