from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Blog, Post, Comment
from .serializable import BlogSerializable, PostSerialize, CommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def blogs(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serialize_blog = BlogSerializable(blog, many=True)
        return Response(serialize_blog.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        req = BlogSerializable(data=request.data)
        req.is_valid(raise_exception=True)
        req.save()
        return Response(data=req.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def blog_detail(request, pk):
    blog = get_object_or_404(klass=Blog, id=pk)
    if request.method == 'GET':
        serialize_blog = BlogSerializable(blog)
        return Response(serialize_blog.data, status=status.HTTP_302_FOUND)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serialize_bug = BlogSerializable(blog, data=request.data)
        serialize_bug.is_valid(raise_exception=True)
        serialize_bug.save()
        return Response(data=serialize_bug.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def posts(request, blogId):
    post = Post.objects.filter(blog_id=blogId)
    serialize_post = PostSerialize(post, many=True)
    return Response(data=serialize_post.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def post_details(request, pk):
    post = get_object_or_404(klass=Post, id=pk)
    if request.method == 'GET':
        serialize_post = PostSerialize(post)
        return Response(data=serialize_post.data, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serialize_post = PostSerialize(post, data=request.data)
        serialize_post.is_valid(raise_exception=True)
        serialize_post.save()
        return Response(data=serialize_post.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_post(request):
    serialize_post = PostSerialize(data=request.data)
    serialize_post.is_valid(raise_exception=True)
    serialize_post.save()
    return Response(data=serialize_post.data, status=status.HTTP_201_CREATED)


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

