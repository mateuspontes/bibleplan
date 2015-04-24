# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20150422_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='planos',
            name='descricao',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='planos',
            name='dias',
            field=models.IntegerField(default=1),
        ),
    ]
