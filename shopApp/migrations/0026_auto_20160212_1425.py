# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0025_auto_20160212_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name=b'*ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(verbose_name=b'*category', blank=True, to='shopApp.Category', null=True),
            preserve_default=True,
        ),
    ]