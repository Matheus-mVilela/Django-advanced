from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.views.generic.list import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


@login_required
def persons_list(request):
    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)

    # busca tem que atender as duas condições para ocorrer.
    # if first_name or last_name:
    #     persons = Person.objects.filter(
    #         first_name__icontains=first_name, last_name__icontains=last_name
    #     )
    # else:
    #     persons = Person.objects.all()

    # buscar um ou outro primeiro pelo nome se nao acher nada busca pelo sobrenome
    if first_name or last_name:
        persons = Person.objects.filter(
            first_name__icontains=first_name
        ) | Person.objects.filter(last_name__icontains=last_name)
    else:
        persons = Person.objects.all()

    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add__person'):
        return HttpResponse('Não autorizado')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    if not request.user.has_perm('clientes.change__person'):
        return HttpResponse('Não autorizado')

    person = get_object_or_404(Person, pk=id)
    form = PersonForm(
        request.POST or None, request.FILES or None, instance=person
    )

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendas'] = Venda.objects.filter(pessoa_id=self.object.id)
        return context


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('personlist')


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('personlist')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.del_person',)

    model = Person

    # success_url = reverse_lazy("personlist")
    def get_success_url(self):
        return reverse_lazy('personlist')


class ProdutoBulk(LoginRequiredMixin, View):
    def get(self, request):
        produtos = [
            'Melão',
            'Melancia',
            'Abacate',
            'Maça',
            'Pera',
            'Uva',
            'Carambola',
        ]
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)
        return HttpResponse('Status_200')

