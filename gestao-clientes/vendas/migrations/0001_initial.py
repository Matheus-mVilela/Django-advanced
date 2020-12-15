# Generated by Django 3.1.4 on 2020-12-15 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '__first__'),
        ('clientes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('desconto', models.FloatField()),
                ('impostos', models.FloatField()),
                ('nfe_emitida', models.BooleanField(default=False)),
                (
                    'pessoa',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to='clientes.person',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='ItenDoPedido',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    'produto',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='produtos.produto',
                    ),
                ),
                (
                    'venda',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='vendas.venda'
                    ),
                ),
            ],
        ),
    ]
