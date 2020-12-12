from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Produto


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.PROTECT
    )
    nfe_emitida = models.BooleanField(default=False)

    # @property
    # def valor(self):
    #    valor = 0
    #    for produto in self.produtos.all():
    #        valor += produto.preco

    #   return (valor - self.desconto) - self.impostos

    def __str__(self):
        return self.numero

    def save(self, *args, **kwargs):
        self.valor = 0
        super(Venda, self).save(*args, **kwargs)
        for produto in self.produtos.all():
            self.valor += produto.preco

        self.valor = (self.valor - self.desconto) - self.impostos

        return super(Venda, self).save(*args, **kwargs)


class ItenDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.BooleanField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

