from django.http import HttpResponse, HttpResponseNotFound


def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound(
            '<h1>Requer permição para esta atividade</h1>'
        )


nfe_emitida.short_description = 'NF-e emitida'


def nfe_nao_emitida(modeladmin, request, queryset):
    if request.user.has_perm('setar_nfe'):
        queryset.update(nfe_emitida=False)
    else:
        return HttpResponseNotFound(
            '<h1>Requer permição para esta atividade</h1>'
        )


nfe_nao_emitida.short_description = 'NF-e não emitida'
