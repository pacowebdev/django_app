from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'pseudo')


admin.site.register(Comment, CommentAdmin)
