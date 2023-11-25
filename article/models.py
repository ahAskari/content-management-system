from re import T
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=1000000)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.pk} - {self.title}'


class ArticlePhoto(models.Model):
    path = models.ImageField(blank=True, null=True, upload_to='media/article')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return f'{self.pk} - {self.path}'
