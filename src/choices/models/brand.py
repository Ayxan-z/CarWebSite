from django.db import models


class BrandModel(models.Model):
    name = models.CharField('name', max_length=25)

    class Meta:
        db_table = 'brand'
        verbose_name_plural = "Brands"
        verbose_name = "Brand"

    def __str__(self) -> str:
        return self.name