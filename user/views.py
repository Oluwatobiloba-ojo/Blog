from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import BlogUser
from .serializer import UserSerializer


# Create your views here.

@api_view(['POST'])
def register(request):
    serialize_user = UserSerializer(data=request.data)
    serialize_user.is_valid(raise_exception=True)
    serialize_user.save()
    return Response(data=serialize_user.data, status=status.HTTP_201_CREATED)
