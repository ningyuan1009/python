from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .serializer_gj import Studentserializergj
from .Serializer import *
from django_vue import settings
from django.http import HttpResponse, JsonResponse
import datetime
import jwt
from .models import User
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        ret = {
            "data": {},
            "meta": {
                "status": 200,
                "message": ""
            }
        }
        try:
            username = request.data['username']
            password = request.data['password']
            value = int(request.data['value'])

            if value == 1:
                user = User.objects.filter(username=username, password=password).first()
                print(username, password, value, user)
                if not user:
                    ret["meta"]["status"] = 500
                    ret["meta"]["message"] = "用户名不存在或密码错误"
                    return Response(ret)
                else:
                    payload = {
                        "exp": datetime.datetime.now() + datetime.timedelta(days=1),
                        "iat": datetime.datetime.now(),
                        "id": user.id,
                        "username": user.username,
                    }

                    ret["data"]["username"] = user.username
                    ret["data"]["id"] = user.id
                    ret["data"]["isAdmin"] = 1  # 假设所有用户都是管理员，这可以根据需要修改
                    ret["meta"]["status"] = 200
                    ret["meta"]["message"] = "登录成功"
                    print(ret, type(ret))
                    return Response(ret)
        except Exception as error:
            print(error)
            ret["meta"]["status"] = 500
            ret["meta"]["message"] = "用户名不存在或密码错误"
            return Response(ret)

class RegisterView(APIView):
    def post(self, request):
        ret = {
            "data": {},
            "meta": {
                "status": 200,
                "message": ""
            }
        }
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            if not username or not password:
                ret["meta"]["status"] = 400
                ret["meta"]["message"] = "用户名和密码不能为空"
                return Response(ret, status=400)

            if User.objects.filter(username=username).exists():
                ret["meta"]["status"] = 400
                ret["meta"]["message"] = "用户名已存在"
                return Response(ret, status=400)

            user = User.objects.create(username=username, password=password)
            ret["data"]["username"] = user.username
            ret["data"]["id"] = user.id
            ret["meta"]["status"] = 201
            ret["meta"]["message"] = "用户注册成功"
            return Response(ret, status=201)
        except Exception as error:
            print(error)
            ret["meta"]["status"] = 500
            ret["meta"]["message"] = "服务器内部错误"
            return Response(ret, status=500)

class ProtectedView(APIView):
            permission_classes = [IsAuthenticated]

            def get(self, request):
                content = {'message': '这是一个受保护的视图，仅认证用户可见。'}
                return Response(content)

class Studentviewgj(APIView):

    def get(self, request):
        students = Student.objects.all()
        print('原生 serializer 改进')
        serializer = Studentserializergj(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('原生 serializer 改进')
        serializer = Studentserializergj(request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response(serializer.errors)



class Studentdetailviewgj(APIView):

    def get(self, request, pk):  # pk的主键值传到这里
        students = Students.objects.get(pk=pk)
        serializer = Studentserializergj(instance = students, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        stu = Student.objects.get(pk=pk)
        ser = Studentserializergj(instance=stu, data=request.data)
        try:
            ser.is_valid(raise_exception=True)
            ser.save()
            return Response(ser.data)
        except Exception as e:
            return Response(ser.errors)

    def delete(self, request, pk):
        Student.objects.get(pk=pk).delete()
        return Response('删除成功')