from django.db import models


class FuelTypeModel(models.Model):
    name = models.CharField('Fuel Type', max_length=20)

    class Meta:
        db_table = 'fuel_type'
        verbose_name_plural = "Fuel Types"
        verbose_name = "Fuel Type"

    def __str__(self) -> str:
        return self.name