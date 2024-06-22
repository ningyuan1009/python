from rest_framework import serializers
from .models import *

class Studentserializergj(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    class_null = serializers.CharField()


    def create(self,validated_data):
        instance = Student.objects.create(**validated_data)
        return instance


    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.sex = validated_data.get('sex',instance.sex)
        instance.age = validated_data.get('age', instance.age)
        instance.class_null = validated_data.get('class_null', instance.class_null)
        instance.save()
        return instance