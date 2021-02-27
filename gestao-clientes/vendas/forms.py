from django import forms


class CriarVendaForm(forms.Form):
    pass


class ProdutosForm(forms.Form):
    produto_id = forms.IntegerField()
    quantidade = forms.IntegerField()
    desconto = forms.FloatField()
