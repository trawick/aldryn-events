# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app_data.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_events', '0019_auto_20150804_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='detail_link',
            field=models.URLField(default='', verbose_name='external link', blank=True, help_text='external link to details about this event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='register_link',
            field=models.URLField(default='', verbose_name='registration link', blank=True, help_text='link to an external registration system'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventlistplugin',
            name='style',
            field=models.CharField(choices=[('standard', 'Standard')], default='standard', verbose_name='Style', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventsconfig',
            name='app_data',
            field=app_data.fields.AppDataField(editable=False, default='{}'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventtranslation',
            name='location',
            field=models.TextField(default='', verbose_name='location', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventtranslation',
            name='short_description',
            field=djangocms_text_ckeditor.fields.HTMLField(default='', verbose_name='short description', blank=True, help_text='translated'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='address',
            field=models.TextField(default='', verbose_name='Address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='company',
            field=models.CharField(default='', verbose_name='Company', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='language_code',
            field=models.CharField(choices=[('en', 'English'), ('ar', 'Arabic'), ('fr', 'French')], default='en', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='message',
            field=models.TextField(default='', verbose_name='Message', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='mobile',
            field=models.CharField(default='', verbose_name='Mobile number', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(default='', verbose_name='Phone number', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='salutation',
            field=models.CharField(choices=[('mrs', 'Ms.'), ('mr', 'Mr.')], default='mrs', verbose_name='Salutation', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='upcomingpluginitem',
            name='style',
            field=models.CharField(choices=[('standard', 'Standard')], default='standard', verbose_name='Style', max_length=50),
            preserve_default=True,
        ),
    ]
