# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0006_user_account_is_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
    ]
