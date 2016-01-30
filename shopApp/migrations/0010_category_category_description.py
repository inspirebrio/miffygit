# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0009_remove_category_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(max_length=800, null=True, blank=True),
            preserve_default=True,
        ),
    ]
