from django.db import models
from .brand import BrandModel


class AutoModelsModel(models.Model):
    name = models.CharField('name', max_length=40)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='auto_models')

    class Meta:
        db_table = 'auto_models'
        verbose_name_plural = "Auto Models"
        verbose_name = "Auto Model"

    def __str__(self) -> str:
        return f'{self.brand.name} -> {self.name}'