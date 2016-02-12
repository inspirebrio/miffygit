# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0019_auto_20160212_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(default=0, verbose_name=b'*category', blank=True, to='shopApp.Category'),
            preserve_default=False,
        ),
    ]
