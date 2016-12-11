# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20160528_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aid', models.IntegerField(default=0)),
                ('atitle', models.CharField(default=b'', max_length=256)),
                ('asubj', models.CharField(default=b'', max_length=128)),
                ('acontent', models.CharField(default=b'', max_length=128)),
                ('areadcount', models.IntegerField(default=0)),
                ('agoodcount', models.IntegerField(default=0)),
                ('acomment', models.CharField(default=b'', max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='vname',
        ),
        migrations.AddField(
            model_name='video',
            name='vid',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='vstage',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='vsubj',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='vurl',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
