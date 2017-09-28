# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='publish-time')),
                ('update_time', models.DateField(auto_now=True, null=True, verbose_name='update-time')),
            ],
        ),
    ]
