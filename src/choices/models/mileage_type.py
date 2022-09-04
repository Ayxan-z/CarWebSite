from django.db import models


class MileageTypeModel(models.Model):
    name = models.CharField('Mileage Type', max_length=5)

    class Meta:
        db_table = 'mileage_type'
        verbose_name_plural = "Mileage Types"
        verbose_name = "Mileage Type"

    def __str__(self) -> str:
        return self.name