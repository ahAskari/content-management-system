from django.db import models


class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment')
    article_id = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comment_of_article')
    created_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'comment'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.pk} - {self.content}'
