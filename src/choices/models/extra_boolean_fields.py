from django.db import models


class ExtraBooleanFieldsModel(models.Model):
    name = models.CharField('Boolean Field', max_length=25, unique=True)

    class Meta:
        db_table = 'extra_boolean_field'
        verbose_name_plural = "Extra Boolean Fields"
        verbose_name = "Extra Boolean Field"

    def __str__(self) -> str:
        return self.name