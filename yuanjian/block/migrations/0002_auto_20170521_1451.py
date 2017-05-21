# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name_plural': '版块', 'verbose_name': '版块'},
        ),
        migrations.AddField(
            model_name='block',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态', choices=[(0, '正常'), (-1, '删除')]),
            preserve_default=False,
        ),
    ]
