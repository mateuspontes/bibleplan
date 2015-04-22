from django.contrib import admin
from plan.models import Livros, Testamentos, Versoes, Versiculos

class VersiculoAdmin(admin.ModelAdmin):
    list_display = ('texto', 'livro', 'versao')
    search_fields = ['texto']

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'abreviacao', 'testamento')
    search_fields = ['nome', 'abreviacao']

class TestamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'book_count')

    def book_count(self, obj):
        return obj.livros_set.count()

admin.site.register(Testamentos, TestamentoAdmin)
admin.site.register(Livros, LivroAdmin)
admin.site.register(Versiculos, VersiculoAdmin)
admin.site.register(Versoes)
