from django.db import models
from django.db.models import Max, Min, Aggregate, Avg, Count


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('valor_total'))['valor_total__avg']

    def max(self):
        return self.all().aggregate(Max('valor_total'))['valor_total__max']

    def min(self):
        return self.all().aggregate(Min('valor_total'))['valor_total__min']

    def num_ped(self):
        return self.all().aggregate(Count('id'))['id__count']

    def nfe_emitida(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))[
            'id__count'
        ]

