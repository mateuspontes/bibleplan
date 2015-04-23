from django.contrib import admin
from . import models

class VersiculoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'livro', 'versao')
    search_fields = ['texto']

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'abreviacao', 'testamento')
    search_fields = ['nome', 'abreviacao']

class TestamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'book_count')

    def book_count(self, obj):
        return obj.livros_set.count()
    book_count.short_description = 'Livros'

class LeituraAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'dia', 'plano')
    search_fields = ['dia']

admin.site.register(models.Testamentos, TestamentoAdmin)
admin.site.register(models.Livros, LivroAdmin)
admin.site.register(models.Versiculos, VersiculoAdmin)
admin.site.register(models.Versoes)
admin.site.register(models.Planos)
admin.site.register(models.Leituras, LeituraAdmin)
