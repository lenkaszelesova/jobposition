# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0033_auto_20150511_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 11, 8, 5, 35, 763133, tzinfo=utc), verbose_name=b'Job created'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='owner',
            field=models.ForeignKey(related_name='jobs', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
