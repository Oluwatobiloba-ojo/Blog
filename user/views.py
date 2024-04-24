from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import BlogUser
from .serializer import UserSerializer, LoginRequestSerializer
from .util.token import createToken


# Create your views here.

@api_view(['POST'])
def register(request):
    serialize_user = UserSerializer(data=request.data)
    serialize_user.is_valid(raise_exception=True)
    serialize_user.save()
    return Response(data=serialize_user.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    serialize_user = LoginRequestSerializer(data=request.data)
    serialize_user.is_valid(raise_exception=True)
    username = serialize_user.data.get('username')
    user: BlogUser = BlogUser.objects.get(username=username)
    if user is None:
        return Response(data="Invalid Details", status=status.HTTP_400_BAD_REQUEST)
    if user.password != serialize_user.data.get('password'):
        return Response(data="Invalid Details", status=status.HTTP_400_BAD_REQUEST)
    token = createToken(user)
    return Response(data=token, status=status.HTTP_200_OK)
