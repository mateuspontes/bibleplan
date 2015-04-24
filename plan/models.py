from __future__ import unicode_literals

from django.db import models

class Livros(models.Model):
    testamento = models.ForeignKey('Testamentos')
    posicao = models.IntegerField()
    nome = models.CharField(max_length=30)
    abreviacao = models.CharField(max_length=5, verbose_name='abreviação')

    class Meta:
        db_table = 'livros'
        verbose_name_plural = 'Livros'
        ordering = ['id']

    def __str__(self):
        return self.nome

class Testamentos(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        db_table = 'testamentos'
        verbose_name_plural = 'Testamentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Versiculos(models.Model):
    versao = models.ForeignKey('Versoes')
    livro = models.ForeignKey(Livros)
    capitulo = models.IntegerField(verbose_name='capítulo')
    versiculo = models.IntegerField(verbose_name='versículo')
    texto = models.TextField()

    class Meta:
        db_table = 'versiculos'
        verbose_name_plural = 'Versículos'

    def __str__(self):
        return "%s:%s - %s" % (self.capitulo, self.versiculo, self.texto)


class Versoes(models.Model):
    nome = models.CharField(max_length=50, verbose_name='nome da versão')

    class Meta:
        db_table = 'versoes'
        verbose_name_plural = 'Versões'

    def __str__(self):
        return self.nome

class Planos(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField(blank=True, null=True)
    dias = models.IntegerField(default=1)

    class Meta:
        db_table = 'planos'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.titulo

class Leituras(models.Model):
    plano = models.ForeignKey(Planos)
    livro = models.ForeignKey(Livros)
    dia = models.IntegerField(blank=False, null=False)
    capitulo = models.IntegerField(verbose_name='capítulo')
    versiculo_inicial = models.IntegerField(verbose_name='versículo inicial')
    versiculo_final = models.IntegerField(verbose_name='versículo final')

    def __str__(self):
        return "Dia %s - %s %s:%s-%s" % (self.dia, self.livro, self.capitulo, self.versiculo_inicial, self.versiculo_final)

    class Meta:
        db_table = 'leituras'
        verbose_name_plural = 'Leituras'

