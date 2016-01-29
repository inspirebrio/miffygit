# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='is_client',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
