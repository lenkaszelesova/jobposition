# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20150509_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 9, 18, 3, 49, 159022, tzinfo=utc), verbose_name=b'Job created'),
        ),
    ]
