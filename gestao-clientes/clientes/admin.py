from django.contrib import admin
from .models import Person, Documento


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
    list_filter = ('age', 'salary')
    # exclude = ('bio',)
    list_display = (
        'first_name',
        'last_name',
        'age',
        'salary',
        'tem_bio',
        'tem_photo',
        'doc',
    )
    search_fields = ('id', 'first_name')

    def tem_photo(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_photo.short_description = 'Possui foto'

    def tem_bio(self, obj):
        if obj.bio:
            return 'Sim'
        else:
            return 'Não'

    tem_bio.short_description = 'Possui bio'


class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'doc_name',
        'num_doc',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
