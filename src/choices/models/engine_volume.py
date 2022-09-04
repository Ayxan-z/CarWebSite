from django.db import models


class EngineVolumeModel(models.Model):
    volume = models.IntegerField('Engine Volume')

    class Meta:
        db_table = 'engine_volume'
        verbose_name_plural = "Engine Volumes"
        verbose_name = "Engine Volume"

    def __str__(self) -> str:
        return str(self.volume)