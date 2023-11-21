from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=1000)
    photo = models.ImageField()
    created_at = models.DateField()
    author_id = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'
        ordering = ['created_at']

    def __str__(self):
        return f'article({self.pk})-{self.title}'
