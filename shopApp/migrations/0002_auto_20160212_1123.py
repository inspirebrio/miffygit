# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner1',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, verbose_name=b'*ad_banner1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner2',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, verbose_name=b'*ad_banner2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_banner3',
            field=models.ImageField(help_text=b"<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>", upload_to=shopApp.models.upload_to1, verbose_name=b'*ad_banner3'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_description',
            field=models.CharField(max_length=500, verbose_name=b'*ad_description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveDateFrom',
            field=models.DateField(default=None, verbose_name=b'*ad_liveDateFrom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveFromTo',
            field=models.DateField(default=None, verbose_name=b'*ad_liveDateTo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_name',
            field=models.CharField(max_length=800, verbose_name=b'*ad_name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_title',
            field=models.CharField(max_length=800, verbose_name=b'*ad_title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(max_length=800, verbose_name=b'*ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url3',
            field=models.URLField(max_length=800, verbose_name=b'*ad_url3'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='banner_position',
            field=models.IntegerField(default=0, verbose_name=b'*banner_position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(verbose_name=b'*category', to='shopApp.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='client',
            field=models.ForeignKey(verbose_name=b'*client', to='shopApp.Client', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='key',
            field=models.CharField(max_length=800, verbose_name=b'*key'),
            preserve_default=True,
        ),
    ]
