from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentRegister(admin.ModelAdmin):
    pass
