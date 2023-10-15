from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
import requests
from rest_framework.views import APIView
# Create your views here.

'''
@api_view()
def hello_world(request):
    return Response({'msg': 'hello world'})
 '''
@api_view(['GET'])
def hello_worlds(request):
    return Response({'msg': 'hello world'})

@api_view(['POST'])
def hello_world(request):
    if request.method == "POST":
        print(request.data)
        return Response({'msg': 'This is Post Request'})

class StudentAPI(APIView):
    def get(self, request, format = None, pk = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self,request, format = None, pk = None ):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format = None):
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,
        partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, format = None, pk = None):
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

@api_view(['GET','POST','PUT','PATCH', "DELETE"])
def student_api(request, pk = None):
    




