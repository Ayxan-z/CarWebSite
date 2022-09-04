from django.db import models


class YearsModel(models.Model):
    year = models.IntegerField('Year')

    class Meta:
        db_table = 'year'
        verbose_name_plural = "Years"
        verbose_name = "Year"

    def __str__(self) -> str:
        return str(self.year)