from django.db import models
from django.conf import settings


# Create your models here.

class Blog(models.Model):
    createdAt = models.DateField(auto_now=True)
    domainName = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} {self.domainName}'


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    createdAt = models.DateField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content = models.CharField(max_length=100)
    created_on = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.author}'
