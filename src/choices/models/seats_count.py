from django.db import models


class SeatsCountModel(models.Model):
    count = models.CharField('Seats Count', max_length=3)

    class Meta:
        db_table = 'seats_count'
        verbose_name_plural = "Seats Count"
        verbose_name = "Seats Count"

    def __str__(self) -> str:
        return self.count