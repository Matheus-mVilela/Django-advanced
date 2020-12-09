from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

    def doc_name(self,):
        return self.person.first_name if self.person else self.num_doc

    doc_name.short_description = 'Titular do Documento'


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(
        upload_to='clients_photos', null=True, blank=True
    )
    doc = models.OneToOneField(
        Documento, null=True, blank=True, on_delete=models.CASCADE
    )

    @property
    def name_full(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao


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


class ItensDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.BooleanField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
