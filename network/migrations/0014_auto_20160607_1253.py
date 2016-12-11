# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_auto_20160607_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.CharField(default=b'', max_length=10000),
            preserve_default=True,
        ),
    ]
