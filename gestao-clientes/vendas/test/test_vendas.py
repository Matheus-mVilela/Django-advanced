from django.test import TestCase
from vendas.models import Venda, ItenDoPedido
from produtos.models import Produto


class VendaTestCase(TestCase):
    def setUp(self):
        self.venda = Venda.objects.create(id='1', desconto=10)
        self.produto = Produto.objects.create(descricao='banana', preco=10)

    def test_verificar_num_vendas(self):
        assert Venda.objects.all().count() == 1

    def test_valor_venda(self):
        ItenDoPedido.objects.create(
            venda=self.venda, produto=self.produto, quantidade=10, desconto=10
        )
        assert self.venda.valor == 80

    def test_desconto(self):
        assert self.venda.desconto == 10

    def add_itens_na_lista(self):
        item = ItemDoPedido.objects.create(
            venda=self.venda, produto=self.produto, quantidade=1, desconto=1
        )

        self.assertIn(item, self.venda.itemdopedido_set.all())

    def test_check_nfe_nao_emitida(self):
        self.assertFalse(self.venda.nfe_emitida)

    def test_check_status(self):
        self.venda.status = 'PC'
        self.venda.save()
        self.assertEqual(self.venda.status, 'PC')
