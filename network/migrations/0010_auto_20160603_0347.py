# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20160602_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='q_id',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t_id',
        ),
    ]
