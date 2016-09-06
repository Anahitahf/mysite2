# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160903_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publicatithon_date',
            new_name='publication_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]
