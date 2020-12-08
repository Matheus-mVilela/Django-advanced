from django.contrib import admin
from .models import Person, Documento, Venda, Produto, ItensDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


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
    search_fields = ('id', 'first_name')

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
    readonly_fields = ('valor',)
    # raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
    list_filter = ('pessoa__doc',)
    list_display = ('id', 'pessoa', 'valor', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    row_id_fields = ('pessoa',)
    actions = [nfe_emitida, nfe_nao_emitida]
    # filter_vertical = ['produtos',]
    # filter_horizontal = ['produtos',]


class ItensDoPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'venda',
        'produto',
        'quantidade',
        'desconto',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto,)
admin.site.register(ItensDoPedido)
