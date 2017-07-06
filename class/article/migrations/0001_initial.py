# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20170521_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='版块名称', max_length=100)),
                ('content', models.CharField(verbose_name='版块描述', max_length=10000)),
                ('status', models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (-1, '删除')])),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('block', models.ForeignKey(verbose_name='版块ID', to='block.Block')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
