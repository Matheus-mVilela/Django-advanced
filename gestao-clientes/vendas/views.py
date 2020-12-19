from django.shortcuts import render
from django.views import View
from vendas.models import Venda
from django.http import HttpResponse


class DashBoard(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado')

        return super(DashBoard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['max'] = Venda.objects.max()
        data['min'] = Venda.objects.min()
        data['media_desconto'] = Venda.objects.media_desconto()
        data['num_ped'] = Venda.objects.num_ped()
        data['nfe_emitida'] = Venda.objects.nfe_emitida()
        return render(request, 'vendas/dashboard.html', data)
