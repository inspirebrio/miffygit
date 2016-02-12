# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0008_auto_20160212_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner1',
            field=models.ImageField(default=0, help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", verbose_name=b'*ad_banner1', upload_to=shopApp.models.upload_to1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner2',
            field=models.ImageField(default=0, help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", verbose_name=b'*ad_banner2', upload_to=shopApp.models.upload_to1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner3',
            field=models.ImageField(default=0, help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", verbose_name=b'*ad_banner3', upload_to=shopApp.models.upload_to1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(blank=True, max_length=800, verbose_name=b'*ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url1',
            field=models.URLField(default=0, max_length=800, verbose_name=b'*ad_url1', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url2',
            field=models.URLField(default=0, max_length=800, verbose_name=b'*ad_url2', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url3',
            field=models.URLField(default=0, max_length=800, verbose_name=b'*ad_url3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(verbose_name=b'*category', blank=True, to='shopApp.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='client',
            field=models.ForeignKey(verbose_name=b'*client', blank=True, to='shopApp.Client', null=True),
            preserve_default=True,
        ),
    ]
