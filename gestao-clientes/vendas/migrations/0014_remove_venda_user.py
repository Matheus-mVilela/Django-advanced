# Generated by Django 3.1.4 on 2021-03-09 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0013_itendopedido_desconto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='user',
        ),
    ]
