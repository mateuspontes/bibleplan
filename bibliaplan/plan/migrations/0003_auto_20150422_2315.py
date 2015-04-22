# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_leituras_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leituras',
            name='dia',
            field=models.IntegerField(),
        ),
    ]
