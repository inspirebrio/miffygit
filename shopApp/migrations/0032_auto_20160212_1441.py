# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0031_auto_20160212_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner1',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, verbose_name=b'*Ad_banner1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner2',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, null=True, verbose_name=b'Ad_banner2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner3',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, null=True, verbose_name=b'Ad_banner3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveDateFrom',
            field=models.DateField(default=None, verbose_name=b'*Ad_liveDateFrom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveFromTo',
            field=models.DateField(default=None, verbose_name=b'*Ad_liveDateTo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='banner_position',
            field=models.IntegerField(default=0, verbose_name=b'*Banner_position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='key',
            field=models.CharField(max_length=800, verbose_name=b'*Key'),
            preserve_default=True,
        ),
    ]
