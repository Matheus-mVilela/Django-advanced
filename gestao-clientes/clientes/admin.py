from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Dados Pessoais',
            {'fields': ('first_name', 'last_name', 'doc', 'salary')},
        ),
        ('Dados Complementares', {'fields': ('age', 'bio', 'photo')}),
    )

    # fields = (
    #    ('first_name', 'last_name'),
    #    ('salary', 'age'),
    #    'bio',
    #    'photo',
    #    'doc',
    # )

    # exclude = ('bio',)
    list_display = (
        'first_name',
        'last_name',
        'age',
        'salary',
        'bio',
        'photo',
        'doc',
    )

    list_filter = ('age', 'salary')


class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)
