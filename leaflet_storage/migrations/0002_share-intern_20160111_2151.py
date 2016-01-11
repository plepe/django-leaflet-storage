# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaflet_storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='share_status',
            field=models.SmallIntegerField(default=1, verbose_name='share status', choices=[(1, 'everyone (public)'), (4, 'logged-in users'), (2, 'anyone with link'), (3, 'editors only')]),
        ),
    ]
