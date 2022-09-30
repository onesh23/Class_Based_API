from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from first_api.models import Student
from first_api.serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.


class get_student(APIView):
    def get(self,request,id=None):
        if id:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,id):
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

