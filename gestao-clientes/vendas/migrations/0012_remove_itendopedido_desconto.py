# Generated by Django 3.1.4 on 2021-03-08 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0011_venda_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itendopedido',
            name='desconto',
        ),
    ]
