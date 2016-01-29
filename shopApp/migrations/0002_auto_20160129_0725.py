# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_description',
            new_name='category_description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cat_name',
            new_name='category_name',
        ),
    ]
