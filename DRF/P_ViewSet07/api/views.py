# ViewSet in Django REST framework
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class StudentViewSet(viewsets.ViewSet):
    def List(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id =id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Created'})
