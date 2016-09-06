# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160903_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2016, 9, 3, 11, 8, 41, 907084, tzinfo=utc), to='books.Author'),
            preserve_default=False,
        ),
    ]
