from rest_framework import serializers

from appBlog.models import Blog, Post


class BlogSerializable(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['domainName', 'createdAt', 'user']


class PostSerialize(serializers.ModelSerializer):
    blog = BlogSerializable()

    class Meta:
        model = Post
        fields = ['title', 'content', 'blog']
