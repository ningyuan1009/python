from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.BooleanField(default=1)
    class_null = models.CharField(max_length=255)
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
