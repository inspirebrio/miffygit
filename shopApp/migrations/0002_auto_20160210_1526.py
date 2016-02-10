# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveDateFrom',
            field=models.DateField(help_text=b"<font color='green'>*Please use the following format: <em>YYYY-MM-DD</em>.</font>", null=True),
        ),
        migrations.AlterField(
            model_name='banneraddpage',
            name='ad_liveFromTo',
            field=models.DateField(help_text=b"<font color='green'>*Please use the following format: <em>YYYY-MM-DD</em>.</font>", null=True),
        ),
    ]
