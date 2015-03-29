# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField()),
                ('postUser_id', models.PositiveIntegerField()),
                ('department', models.CharField(max_length=2, default='NA')),
                ('grade', models.CharField(max_length=1, default='0')),
                ('pub_date', models.DateTimeField()),
                ('process_status', models.CharField(max_length=1, default='N')),
                ('subscribe_num', models.PositiveIntegerField(default=0)),
                ('public', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('reply_user_id', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('appeal', models.ForeignKey(to='mainapp.Appeal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('subscribe_user_id', models.PositiveIntegerField()),
                ('appeal', models.ForeignKey(to='mainapp.Appeal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
