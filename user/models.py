from django.db import models
from article.models import Article
from comment.models import Comment


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    avatar = models.ImageField(blank=True, null=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user'
        ordering = ['username']

    def __str__(self):
        return f'user({self.pk})-{self.username}'
