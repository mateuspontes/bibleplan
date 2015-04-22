from __future__ import unicode_literals

from django.db import models

class Livros(models.Model):
    testamento = models.ForeignKey('Testamentos')
    posicao = models.IntegerField()
    nome = models.CharField(max_length=30)
    abreviacao = models.CharField(max_length=5, verbose_name = 'abreviação')

    class Meta:
        managed = False
        db_table = 'livros'
        verbose_name_plural = 'Livros'
        ordering = ['id']

    def __str__(self):
        return self.nome

class Testamentos(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'testamentos'
        verbose_name_plural = 'Testamentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Versiculos(models.Model):
    versao = models.ForeignKey('Versoes')
    livro = models.ForeignKey(Livros)
    capitulo = models.IntegerField(verbose_name = 'capítulo')
    versiculo = models.IntegerField(verbose_name = 'versículo')
    texto = models.TextField()

    class Meta:
        managed = False
        db_table = 'versiculos'
        verbose_name_plural = 'Versículos'

    def __str__(self):
        return "%s:%s - %s" % (self.capitulo, self.versiculo, self.texto)


class Versoes(models.Model):
    vrs_id = models.AutoField(primary_key=True)
    vrs_nome = models.CharField(max_length=50, verbose_name = 'nome da versão')

    class Meta:
        managed = False
        db_table = 'versoes'
        verbose_name_plural = 'Versões'

    def __str__(self):
        return self.vrs_nome