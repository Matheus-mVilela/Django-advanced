from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string


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

    class Meta:
        permissions = (('del_person', 'Apagar User'),)

    @property
    def name_full(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)

        data = {'cliente': self.first_name}
        email_txt = render_to_string('clientes/email/novo_cliente.txt', data)
        email_html = render_to_string('clientes/email/novo_cliente.html', data)

        send_mail(
            'Novo cliente cadastrado.',
            email_txt,
            'matheusvao15@gmail.com',
            ['matheus_vilela@icloud.com'],
            html_message=email_html,
            fail_silently=True,
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

