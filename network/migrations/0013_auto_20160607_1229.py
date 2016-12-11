# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answers',
            new_name='ItemA',
        ),
        migrations.AddField(
            model_name='question',
            name='ItemB',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='ItemC',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='ItemD',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='rightAnswer',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
