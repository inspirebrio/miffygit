# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_auto_20160129_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner1',
            field=models.ImageField(null=True, upload_to=shopApp.models.upload_to1, blank=True),
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner2',
            field=models.ImageField(null=True, upload_to=shopApp.models.upload_to1, blank=True),
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner3',
            field=models.ImageField(null=True, upload_to=shopApp.models.upload_to1, blank=True),
        ),
    ]
