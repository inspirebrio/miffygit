# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0010_auto_20160212_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(max_length=800, verbose_name=b'*ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
    ]
