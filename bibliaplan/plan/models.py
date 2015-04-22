from __future__ import unicode_literals

from django.db import models


class Livros(models.Model):
    testamento = models.ForeignKey('Testamentos')
    posicao = models.IntegerField()
    nome = models.CharField(max_length=30)
    abreviacao = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'livros'

class Testamentos(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'testamentos'


class Versiculos(models.Model):
    versao_id = models.IntegerField()
    livro = models.ForeignKey(Livros)
    capitulo = models.IntegerField()
    versiculo = models.IntegerField()
    texto = models.TextField()

    class Meta:
        managed = False
        db_table = 'versiculos'


class Versoes(models.Model):
    vrs_id = models.AutoField(primary_key=True)
    vrs_nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'versoes'
