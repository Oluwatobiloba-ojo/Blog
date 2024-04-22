import datetime

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
    createdAt = models.DateField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.pk is None:
            self.createdAt = datetime.date.today()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_on = models.DateField()
    updated_on = models.DateField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.pk is None:
            self.created_on = datetime.date.today()
        else:
            self.created_on = self.created_on
            self.updated_on = datetime.date.today()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.author}'
