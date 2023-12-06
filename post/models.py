from django.db import models


class Post(models.Model):
    title_fa = models.CharField(max_length=120)
    title_ar = models.CharField(max_length=120, blank=True)
    title_en = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now=True)
    content_fa = models.CharField(max_length=1000000, blank=True)
    content_ar = models.CharField(max_length=1000000, blank=True)
    content_en = models.CharField(max_length=1000000, blank=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='post')
    tags = models.ManyToManyField('tag.Tag', blank=True, related_name='post')
    category = models.ForeignKey('category.Category', blank=True, null=True, related_name='post', on_delete=models.CASCADE)
    photos = models.ManyToManyField('media.Photo', blank=True, related_name='post')

    class Meta:
        db_table = 'post'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.pk} - {self.title_fa}'
