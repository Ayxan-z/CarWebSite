from django.db import models


class ColorModel(models.Model):
    name = models.CharField('Color', max_length=15)

    class Meta:
        db_table = 'color'
        verbose_name_plural = "Colors"
        verbose_name = "Color"

    def __str__(self) -> str:
        return self.name