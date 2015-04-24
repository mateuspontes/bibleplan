# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_auto_20150424_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planos',
            name='dias',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
