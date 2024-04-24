from rest_framework import serializers

from appBlog.models import Blog, Post, Comment


class BlogSerializable(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['domainName', 'createdAt']

    def create(self, validated_data):
        user = self.context
        blog = Blog.objects.create(user=user, **validated_data)
        return blog


class PostSerialize(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def create(self, validated_data):
        blog_id = self.context
        return Post.objects.create(blog_id=blog_id, **validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'post']
