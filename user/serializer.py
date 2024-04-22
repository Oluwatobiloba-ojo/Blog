from rest_framework import serializers
from .models import BlogUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = ['username', 'email', 'password', 'date_of_birth']

