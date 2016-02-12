# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0026_auto_20160212_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_title',
            field=models.CharField(max_length=800, null=True, verbose_name=b'*ad_title'),
            preserve_default=True,
        ),
    ]
