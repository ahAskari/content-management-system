from django.db import models


class Comment(models.Model):
    content = models.CharField(max_length=200)
    auther_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateField()

    class Meta:
        db_table = 'comment'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.pk}'
