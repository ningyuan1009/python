from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models

class UserSerializer(ModelSerializer):
    username = serializers.CharField(read_only=True)
    class Meta:
        model = models.User
        fields = '__all__'