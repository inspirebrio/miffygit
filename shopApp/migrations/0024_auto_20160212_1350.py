# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0023_auto_20160212_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_name',
            field=models.CharField(max_length=800, null=True, verbose_name=b'*ad_name'),
            preserve_default=True,
        ),
    ]
