from django.contrib import admin
from .models import Venda
from .models import ItenDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


# class ItenDopedidoInline(admin.TabularInline):
#   model = ItenDoPedido
#  extra = 1


class ItenDopedidoInline(admin.StackedInline):
    model = ItenDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    # raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
    list_filter = ('pessoa__doc',)
    list_display = ('id', 'pessoa', 'valor', 'nfe_emitida', 'valor_total')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    row_id_fields = ('pessoa',)
    exclude = ('valor_total', 'user')
    actions = [nfe_emitida, nfe_nao_emitida]
    # filter_vertical = ['produtos',]
    # filter_horizontal = ['produtos',]
    inlines = [ItenDopedidoInline]


class ItensDoPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'venda',
        'produto',
        'quantidade',
        'desconto',
    )


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItenDoPedido)
