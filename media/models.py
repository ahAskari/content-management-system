from django.db import models


class Photo(models.Model):
    path = models.ImageField(max_length=1000, upload_to='photos')

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return f'{self.pk} - {self.path}'
