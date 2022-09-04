from django.db import models


class CategoryModel(models.Model):
    name = models.CharField('name', max_length=25)

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self) -> str:
        return self.name