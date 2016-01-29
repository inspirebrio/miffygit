# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_auto_20160129_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_description',
            new_name='cat_description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='cat_name',
        ),
    ]
