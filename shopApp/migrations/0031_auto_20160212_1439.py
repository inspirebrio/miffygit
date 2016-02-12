# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0030_auto_20160212_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_description',
            field=models.CharField(max_length=500, verbose_name=b'*Ad_description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_name',
            field=models.CharField(max_length=800, verbose_name=b'*Ad_name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_status',
            field=models.BooleanField(default=True, verbose_name=b'Ad_status', choices=[(True, b'Live'), (False, b'Pause')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_title',
            field=models.CharField(max_length=800, verbose_name=b'*Ad_title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(max_length=800, verbose_name=b'*Ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(verbose_name=b'*Category', to='shopApp.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='client',
            field=models.ForeignKey(verbose_name=b'*Client', to='shopApp.Client'),
            preserve_default=True,
        ),
    ]
