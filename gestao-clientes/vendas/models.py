from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Produto
from django.db.models import Sum, F, FloatField, Max, Aggregate


class Venda(models.Model):
    valor_total = models.FloatField(null=True)
    desconto = models.FloatField()
    impostos = models.FloatField()
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    @property
    def valor(self):

        tot = self.itendopedido_set.all().aggregate(
            tot_ped=Sum(
                (F('quantidade') * F('produto__preco')) - F('desconto'),
                output_field=FloatField(),
            )
        )['tot_ped']

        if tot:
            return tot - self.desconto - self.impostos
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

    def __str__(self):
        return f'{self.venda.pk}-{self.produto.descricao}'
