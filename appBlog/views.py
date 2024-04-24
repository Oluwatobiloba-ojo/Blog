from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Blog, Post, Comment
from .serializable import BlogSerializable, PostSerialize, CommentSerializer


class BlogList(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializable

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return self.request.user


# Create your views here.

class PostList(ModelViewSet):
    serializer_class = PostSerialize

    def get_queryset(self):
        return Post.objects.filter(blog=self.kwargs['appBlogs_pk'])

    def get_serializer_context(self):
        return self.kwargs['appBlogs_pk']



@api_view(['GET'])
def comments(request, postId):
    comment = Comment.objects.filter(post_id=postId)
    serialize = CommentSerializer(comment, many=True)
    if len(serialize.data) == 0:
        return Response(data="No comment added yet", status=status.HTTP_404_NOT_FOUND)
    return Response(data=serialize.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_comment(request):
    serialize_comment = CommentSerializer(data=request.data)
    serialize_comment.is_valid(raise_exception=True)
    serialize_comment.save()
    return Response(data=serialize_comment.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE', 'GET'])
def comment_details(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        serialize_comment = CommentSerializer(comment)
        return Response(data=serialize_comment.data, status=status.HTTP_302_FOUND)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serialize_comment = CommentSerializer(comment, data=request.data)
        serialize_comment.is_valid(raise_exception=True)
        serialize_comment.save()
        return Response(data=serialize_comment.data, status=status.HTTP_200_OK)
