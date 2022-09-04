from django.db import models


class TransmissionModel(models.Model):
    name = models.CharField('Transmission', max_length=20)

    class Meta:
        db_table = 'transmission'
        verbose_name_plural = "Transmissions"
        verbose_name = "Transmission"

    def __str__(self) -> str:
        return self.name