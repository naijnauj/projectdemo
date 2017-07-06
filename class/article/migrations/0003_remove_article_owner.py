# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='owner',
        ),
    ]
