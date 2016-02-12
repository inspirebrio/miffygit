# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0021_auto_20160212_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner1',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, verbose_name=b'*ad_banner1', blank=True),
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
            field=models.CharField(max_length=500, verbose_name=b'*ad_description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_name',
            field=models.CharField(max_length=800, verbose_name=b'*ad_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_title',
            field=models.CharField(max_length=800, verbose_name=b'*ad_title', blank=True),
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
            name='category',
            field=models.ForeignKey(verbose_name=b'*category', blank=True, to='shopApp.Category'),
            preserve_default=True,
        ),
    ]
