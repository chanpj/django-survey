# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.db import migrations, models
from future import standard_library

standard_library.install_aliases()


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='template',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
