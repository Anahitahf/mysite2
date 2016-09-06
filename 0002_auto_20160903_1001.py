# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2016, 9, 3, 10, 1, 41, 698255, tzinfo=utc), to='books.Author'),
            preserve_default=False,
        ),
    ]
