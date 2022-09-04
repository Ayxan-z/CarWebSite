from django.db import models


class PriceTypeModel(models.Model):
    name = models.CharField('Price Type', max_length=7)

    class Meta:
        db_table = 'price_type'
        verbose_name_plural = "Price Types"
        verbose_name = "Price Type"

    def __str__(self) -> str:
        return self.name