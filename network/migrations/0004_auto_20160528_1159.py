# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20160528_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('commentdate', models.DateField()),
                ('commentcontent', models.CharField(default=b'', max_length=1280)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('article', models.CharField(default=b'', max_length=128)),
                ('video', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('mstunum', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('sex', models.CharField(default=b'', max_length=128)),
                ('school', models.CharField(default=b'', max_length=128)),
                ('grade', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('title', models.CharField(default=b'', max_length=256)),
                ('subj', models.CharField(default=b'', max_length=128)),
                ('stage', models.CharField(default=b'', max_length=128)),
                ('content', models.CharField(default=b'', max_length=1280)),
                ('answers', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('subj', models.CharField(default=b'', max_length=128)),
                ('score', models.IntegerField(default=0)),
                ('testdate', models.DateField()),
                ('rand', models.IntegerField(default=0)),
                ('level', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('passwd', models.CharField(default=b'', max_length=128)),
                ('liimit', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='acomment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='acontent',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='agoodcount',
            new_name='goodcount',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='aid',
            new_name='mid',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='areadcount',
            new_name='readcount',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='asubj',
            new_name='subj',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='atitle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vid',
            new_name='mid',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vstage',
            new_name='stage',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vsubj',
            new_name='subj',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vurl',
            new_name='url',
        ),
    ]
