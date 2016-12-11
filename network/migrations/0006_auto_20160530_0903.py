# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='readcount',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default=b'', unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
