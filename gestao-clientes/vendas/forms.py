from django import forms


class VendaForm(forms.Form):
    venda_id = forms.IntegerField()
    pessoa_id = forms.IntegerField()
    desconto = forms.FloatField(label='Desconto')
    imposto = forms.FloatField(label='Iposto')
