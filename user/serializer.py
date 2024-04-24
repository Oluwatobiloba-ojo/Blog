from rest_framework import serializers
from .models import BlogUser


class UserSerializer(serializers.BaseSerializer):
    class Meta:
        model = BlogUser
        fields = ['username', 'email', 'password', 'date_of_birth']


class LoginRequestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=120)

    class Meta:
        model = BlogUser
        fields = ['username', 'password']
