from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Blog, Post
from rest_framework.response import Response


from .serializable import BlogSerializable, PostSerialize


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


@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serialize_post = PostSerialize(post, many=True)
        return Response(data=serialize_post.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialize_post = PostSerialize(data=request.data)
        serialize_post.is_valid(raise_exception=True)
        serialize_post.save()
        return Response(data=serialize_post.data, status=status.HTTP_201_CREATED)


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

