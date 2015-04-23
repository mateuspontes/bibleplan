# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leituras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('capitulo', models.IntegerField(verbose_name='capítulo')),
                ('versiculo_inicial', models.IntegerField(verbose_name='versículo inicial')),
                ('versiculo_final', models.IntegerField(verbose_name='versículo final')),
            ],
            options={
                'verbose_name_plural': 'Leituras',
                'db_table': 'leituras',
            },
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('posicao', models.IntegerField()),
                ('nome', models.CharField(max_length=30)),
                ('abreviacao', models.CharField(max_length=5, verbose_name='abreviação')),
            ],
            options={
                'verbose_name_plural': 'Livros',
                'ordering': ['id'],
                'db_table': 'livros',
            },
        ),
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Planos',
                'db_table': 'planos',
            },
        ),
        migrations.CreateModel(
            name='Testamentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Testamentos',
                'ordering': ['nome'],
                'db_table': 'testamentos',
            },
        ),
        migrations.CreateModel(
            name='Versiculos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('capitulo', models.IntegerField(verbose_name='capítulo')),
                ('versiculo', models.IntegerField(verbose_name='versículo')),
                ('texto', models.TextField()),
                ('livro', models.ForeignKey(to='plan.Livros')),
            ],
            options={
                'verbose_name_plural': 'Versículos',
                'db_table': 'versiculos',
            },
        ),
        migrations.CreateModel(
            name='Versoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome da versão')),
            ],
            options={
                'verbose_name_plural': 'Versões',
                'db_table': 'versoes',
            },
        ),
        migrations.AddField(
            model_name='versiculos',
            name='versao',
            field=models.ForeignKey(to='plan.Versoes'),
        ),
        migrations.AddField(
            model_name='livros',
            name='testamento',
            field=models.ForeignKey(to='plan.Testamentos'),
        ),
        migrations.AddField(
            model_name='leituras',
            name='livro',
            field=models.ForeignKey(to='plan.Livros'),
        ),
        migrations.AddField(
            model_name='leituras',
            name='plano',
            field=models.ForeignKey(to='plan.Planos'),
        ),
    ]
