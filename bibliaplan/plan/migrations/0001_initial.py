# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('posicao', models.IntegerField()),
                ('nome', models.CharField(max_length=30)),
                ('abreviacao', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'livros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Testamentos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'testamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Versiculos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('versao_id', models.IntegerField()),
                ('capitulo', models.IntegerField()),
                ('versiculo', models.IntegerField()),
                ('texto', models.TextField()),
            ],
            options={
                'db_table': 'versiculos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Versoes',
            fields=[
                ('vrs_id', models.AutoField(primary_key=True, serialize=False)),
                ('vrs_nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'versoes',
                'managed': False,
            },
        ),
    ]
