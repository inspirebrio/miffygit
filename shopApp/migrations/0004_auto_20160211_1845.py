# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=950, null=True, verbose_name=b"<font color='red'>*</font>address", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='user_account',
            field=models.OneToOneField(related_name='Client', verbose_name=b'*user_account', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
