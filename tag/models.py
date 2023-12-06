from django.db import models


class Tag(models.Model):
    name_fa = models.CharField(max_length=20, unique=True)
    name_ar = models.CharField(max_length=20, blank=True, unique=True)
    name_en = models.CharField(max_length=20, blank=True, unique=True)

    class Meta:
        db_table = 'tag'

    def __str__(self) -> str:
        return f'{self.pk} - {self.name_en}'
