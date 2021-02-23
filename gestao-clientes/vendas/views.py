from django import shortcuts, views
from django.views import View
from vendas.models import Venda
from django.http import HttpResponse
from . import forms
from clientes.models import Person


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

        return shortcuts.render(request, 'vendas/dashboard.html', data,)


class Vendas(views.View):
    def get(self, request):
        person = Person.objects.all()
        venda = forms.VendaForm()
        venda_list = Venda.objects.all()

        return shortcuts.render(
            request,
            'testevendas.html',
            context={
                'venda': venda,
                'person': person,
                'venda_list': venda_list,
            },
        )

