# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0007_remove_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
