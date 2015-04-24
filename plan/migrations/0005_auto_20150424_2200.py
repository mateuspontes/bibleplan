# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20150424_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leituras',
            name='versiculo_final',
            field=models.IntegerField(blank=True, verbose_name='versículo final', null=True),
        ),
        migrations.AlterField(
            model_name='leituras',
            name='versiculo_inicial',
            field=models.IntegerField(blank=True, verbose_name='versículo inicial', null=True),
        ),
    ]
