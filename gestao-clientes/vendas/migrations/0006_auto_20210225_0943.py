# Generated by Django 3.1.4 on 2021-02-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_venda_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='numero',
        ),
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('finished', 'Finished')], default='open', max_length=20),
        ),
    ]
