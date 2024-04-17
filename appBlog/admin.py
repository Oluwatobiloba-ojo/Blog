from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['domainName', 'user', 'createdAt']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_on']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'createdAt']
