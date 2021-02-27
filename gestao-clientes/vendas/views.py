from django import shortcuts, views
from django.views import View
from django.http import HttpResponse
from clientes.models import Person
from vendas.models import Venda, ItenDoPedido
from produtos.models import Produto
from vendas import choices, forms


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


class CreateVendaView(views.View):
    def get(self, request):
        produto = Produto.objects.all().order_by('-id')
        produto_form = forms.ProdutosForm()

        return shortcuts.render(
            request,
            'createvenda.html',
            context={'produto': produto, 'produto_form': produto_form,},
        )

    def post(self, request):
        produto_form = forms.ProdutosForm(request.POST)

        if not produto_form.is_valid:
            return

        venda = Venda.objects.create(user_id=request.user.pk)
        item = ItenDoPedido.objects.create(
            venda=venda,
            produto_id=produto_form.data['produto_id'],
            quantidade=produto_form.data['quantidade'],
            desconto=produto_form.data['desconto'],
        )
        venda.valor_total = item.produto.preco * item.quantidade
        venda.save()
        return shortcuts.redirect('/admin/vendas/vendas')
