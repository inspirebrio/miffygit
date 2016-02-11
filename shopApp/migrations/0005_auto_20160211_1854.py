# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_auto_20160211_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner1',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, null=True, verbose_name=b'*ad_banner1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner2',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, null=True, verbose_name=b'*ad_banner2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner3',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, null=True, verbose_name=b'*ad_banner3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_description',
            field=models.CharField(max_length=500, null=True, verbose_name=b'*ad_description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveDateFrom',
            field=models.DateField(default=None, null=True, verbose_name=b'*ad_liveDateFrom', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveFromTo',
            field=models.DateField(default=None, null=True, verbose_name=b'*ad_liveDateTo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_name',
            field=models.CharField(max_length=800, null=True, verbose_name=b'*ad_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_status',
            field=models.BooleanField(default=True, verbose_name=b'*ad_status', choices=[(True, b'Live'), (False, b'Pause')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_title',
            field=models.CharField(max_length=800, null=True, verbose_name=b'*ad_title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name=b'*ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url1',
            field=models.URLField(max_length=800, null=True, verbose_name=b'*ad_url1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url2',
            field=models.URLField(max_length=800, null=True, verbose_name=b'*ad_url2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url3',
            field=models.URLField(max_length=800, null=True, verbose_name=b'*ad_url3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='banner_position',
            field=models.IntegerField(default=0, null=True, verbose_name=b'*banner_position', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(verbose_name=b'*category', blank=True, to='shopApp.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='client',
            field=models.ForeignKey(verbose_name=b'*client', blank=True, to='shopApp.Client', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='key',
            field=models.CharField(max_length=800, null=True, verbose_name=b'*key', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=950, null=True, blank=True),
            preserve_default=True,
        ),
    ]
