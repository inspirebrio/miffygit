# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_auto_20160130_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_account',
            name='is_client',
        ),
    ]
