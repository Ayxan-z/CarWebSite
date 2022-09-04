from django.db import models


class GearModel(models.Model):
    name = models.CharField('Gear', max_length=15)

    class Meta:
        db_table = 'gear'
        verbose_name_plural = "Gears"
        verbose_name = "Gear"

    def __str__(self) -> str:
        return self.name