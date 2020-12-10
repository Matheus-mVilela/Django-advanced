from django.contrib import admin
from .models import Venda
from .models import ItensDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


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


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
