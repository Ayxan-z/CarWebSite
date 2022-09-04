from django.db import models


class PriorOwnersCountModel(models.Model):
    name = models.CharField('Prior Owners Count', max_length=35)

    class Meta:
        db_table = 'prior_owners_count'
        verbose_name_plural = "Prior Owners Count"
        verbose_name = "Prior Owners Count"

    def __str__(self) -> str:
        return self.name