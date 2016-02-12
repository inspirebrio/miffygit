# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0027_auto_20160212_1426'),
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
            name='ad_description',
            field=models.CharField(max_length=500, verbose_name=b'*ad_description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_name',
            field=models.CharField(default=0, max_length=800, verbose_name=b'*ad_name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_title',
            field=models.CharField(default=0, max_length=800, verbose_name=b'*ad_title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_type',
            field=models.CharField(default=0, max_length=800, verbose_name=b'*ad_type', choices=[(b'text', b'text'), (b'image', b'image')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_url1',
            field=models.URLField(max_length=800, verbose_name=b'*ad_url1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(default=0, verbose_name=b'*category', to='shopApp.Category'),
            preserve_default=False,
        ),
    ]
