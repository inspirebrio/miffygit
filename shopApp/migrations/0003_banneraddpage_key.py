# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_remove_banneraddpage_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='banneraddpage',
            name='key',
            field=models.CharField(max_length=800, null=True, blank=True),
            preserve_default=True,
        ),
    ]
