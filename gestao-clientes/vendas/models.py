from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Produto
from .managers import VendaManager
from django.db.models import Sum, F, FloatField, Max, Aggregate, Avg
from django.contrib.auth.models import User


class Venda(models.Model):
    ABERTA = 'AB'
    FECHADA = 'FC'
    PROCESSANDO = 'PC'

    STATUS = [
        (ABERTA, 'Aberta'),
        (FECHADA, 'Fechada'),
        (PROCESSANDO, 'Processando'),
    ]

    valor_total = models.FloatField(null=True)
    pessoa = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.PROTECT
    )
    nfe_emitida = models.BooleanField(default=False)

    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT
    )
    status = models.CharField(
        choices=STATUS, default=PROCESSANDO, max_length=2
    )

    objects = VendaManager()

    class Meta:
        permissions = (
            ('setar_nfe', 'User set NF-e'),
            ('ver_dashboard', 'Pode ver o DASHBOARD'),
        )

    @property
    def valor(self):

        tot = self.itendopedido_set.all().aggregate(
            tot_ped=Sum(
                (F('quantidade') * F('produto__preco')),
                output_field=FloatField(),
            )
        )['tot_ped']

        if tot:
            return tot
        else:
            return 0

    # @property
    # def valor(self):
    #    valor = 0
    #    for produto in self.produtos.all():
    #        valor += produto.preco

    #   return (valor - self.desconto) - self.impostos

    def __str__(self):

        return f'{self.pk}'

    def save(self, *args, **kwargs):

        super(Venda, self).save(*args, **kwargs)
        tot = self.itendopedido_set.all().aggregate(
            tot_ped=Sum(
                (F('quantidade') * F('produto__preco')) - F('desconto'),
                output_field=FloatField(),
            )
        )['tot_ped']

        if tot:
            self.valor_total = tot - self.desconto - self.impostos
        else:
            self.valor_total = 0

        return super(Venda, self).save(*args, **kwargs)


class ItenDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
        unique_together = ('venda', 'produto')

    def __str__(self):
        return f'{self.venda.pk}-{self.produto.descricao}'
