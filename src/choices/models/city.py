from django.db import models


class CityModel(models.Model):
    name = models.CharField('City', max_length=30)

    class Meta:
        db_table = 'city'
        verbose_name_plural = "Cities"
        verbose_name = "City"

    def __str__(self) -> str:
        return self.name