# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20160102_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
            preserve_default=False,
        ),
    ]