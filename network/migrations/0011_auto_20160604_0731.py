# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20160603_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('count', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=b'', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('count', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=b'', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='video',
            name='mid',
        ),
    ]
