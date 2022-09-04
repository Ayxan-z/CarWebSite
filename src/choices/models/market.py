from django.db import models


class MarketModel(models.Model):
    name = models.CharField('market Name', max_length=30)

    class Meta:
        db_table = 'market'
        verbose_name_plural = "Markets"
        verbose_name = "Market"

    def __str__(self) -> str:
        return self.name