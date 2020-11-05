from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, "person.html", {"persons": persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("person_list")
    return render(request, "person_form.html", {"form": form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(
        request.POST or None, request.FILES or None, instance=person
    )

    if form.is_valid():
        form.save()
        return redirect("person_list")

    return render(request, "person_form.html", {"form": form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == "POST":
        person.delete()
        return redirect("person_list")

    return render(request, "person_delete_confirm.html", {"person": person})


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person


class PersonCreate(CreateView):
    model = Person
    fields = ["first_name", "last_name", "age", "salary", "bio", "photo"]
    success_url = reverse_lazy("personlist")


class PersonUpdate(UpdateView):
    model = Person
    fields = ["first_name", "last_name", "age", "salary", "bio", "photo"]
    success_url = reverse_lazy("personlist")


class PersonDelete(DeleteView):
    model = Person
    # success_url = reverse_lazy("personlist")
    def get_success_url(self):

        return reverse_lazy("personlist")
