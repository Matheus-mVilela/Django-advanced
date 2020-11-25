from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Dados Pessoais',
            {'fields': ('first_name', 'last_name', 'doc', 'salary')},
        ),
        ('Dados Complementares', {'fields': ('age', 'bio', 'photo')}),
    )

    # fields = (
    #    ('first_name', 'last_name'),
    #    ('salary', 'age'),
    #    'bio',
    #    'photo',
    #    'doc',
    # )
    list_filter = ('age', 'salary')
    # exclude = ('bio',)
    list_display = (
        'first_name',
        'last_name',
        'age',
        'salary',
        'tem_bio',
        'tem_photo',
        'doc',
    )

    def tem_photo(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_photo.short_description = 'Possui foto'

    def tem_bio(self, obj):
        if obj.bio:
            return 'Sim'
        else:
            return 'Não'

    tem_bio.short_description = 'Possui bio'


class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc',)
    list_display = ('id', 'pessoa', 'total_venda')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    row_id_fields = ('pessoa',)

    def total_venda(self, obj):
        return obj.get_total()

    total_venda.short_description = 'Total de Vendas'


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)
