# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, unique=True, null=True, blank=True)),
                ('username', models.CharField(max_length=200, unique=True, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('mobile', models.CharField(max_length=15, null=True, blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BannerAddPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ad_name', models.CharField(max_length=200, null=True)),
                ('ad_title', models.CharField(max_length=200, null=True)),
                ('ad_description', models.CharField(max_length=500)),
                ('ad_status', models.BooleanField(default=True, choices=[(True, b'Live'), (False, b'Pause')])),
                ('ad_banner1', models.ImageField(null=True, upload_to=shopApp.models.upload_to1, blank=True)),
                ('ad_url1', models.URLField(null=True, blank=True)),
                ('ad_banner2', models.ImageField(null=True, upload_to=shopApp.models.upload_to1, blank=True)),
                ('ad_url2', models.URLField(null=True, blank=True)),
                ('ad_banner3', models.ImageField(null=True, upload_to=shopApp.models.upload_to1, blank=True)),
                ('ad_url3', models.URLField(null=True, blank=True)),
                ('ad_liveDateFrom', models.DateField(null=True)),
                ('ad_liveFromTo', models.DateField(null=True)),
                ('banner_position', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=200, null=True, blank=True)),
                ('category_description', models.CharField(max_length=800, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=950, null=True, blank=True)),
                ('user_account', models.OneToOneField(related_name=b'Client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='banneraddpage',
            name='category',
            field=models.ForeignKey(to='shopApp.Category', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='banneraddpage',
            name='client',
            field=models.ForeignKey(to='shopApp.Client'),
            preserve_default=True,
        ),
    ]
