# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20160530_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q_id', models.IntegerField(default=1)),
                ('content', models.CharField(default=b'', max_length=1280)),
                ('answers', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('t_id', models.IntegerField(default=1)),
                ('subj', models.CharField(default=b'', max_length=128)),
                ('title', models.CharField(default=b'', max_length=256)),
                ('stage', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
