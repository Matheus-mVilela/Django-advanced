# Generated by Django 3.1.4 on 2020-12-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda', name='valor_total', field=models.FloatField(null=True),
        ),
    ]
