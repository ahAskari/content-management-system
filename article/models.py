from django.db import models


class Tags(models.Model):
    name_fa = models.CharField(max_length=20)
    name_ar = models.CharField(max_length=20, blank=True)
    name_en = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return f'{self.pk} - {self.name_fa}'


class Article(models.Model):
    title_fa = models.CharField(max_length=120)
    title_ar = models.CharField(max_length=120, blank=True)
    title_en = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now=True)
    content_fa = models.CharField(max_length=1000000, blank=True)
    content_ar = models.CharField(max_length=1000000, blank=True)
    content_en = models.CharField(max_length=1000000, blank=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='article')
    tags = models.ManyToManyField(Tags, blank=True, related_name='article')
    photos = models.ManyToManyField('media.Photo', blank=True, related_name='article')

    class Meta:
        db_table = 'article'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.pk} - {self.title_fa}'
