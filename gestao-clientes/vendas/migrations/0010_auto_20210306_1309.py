# Generated by Django 3.1.4 on 2021-03-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0009_auto_20210306_1252'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itendopedido',
            unique_together={('venda', 'produto')},
        ),
    ]
