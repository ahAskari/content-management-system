from django.db import models


class Category(models.Model):
    name_fa = models.CharField(max_length=20, unique=True)
    name_ar = models.CharField(max_length=20, blank=True, unique=True)
    name_en = models.CharField(max_length=20, blank=True, unique=True)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return f'{self.pk} - {self.name_en}'
