from django.contrib import admin
from plan.models import Livros, Testamentos, Versoes, Versiculos, Planos, Leituras

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
    list_display = ('__str__', 'plano')

admin.site.register(Testamentos, TestamentoAdmin)
admin.site.register(Livros, LivroAdmin)
admin.site.register(Versiculos, VersiculoAdmin)
admin.site.register(Versoes)
admin.site.register(Planos)
admin.site.register(Leituras, LeituraAdmin)
