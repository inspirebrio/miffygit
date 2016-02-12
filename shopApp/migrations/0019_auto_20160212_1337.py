# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0018_auto_20160212_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(verbose_name=b'*category', to='shopApp.Category', null=True),
            preserve_default=True,
        ),
    ]
