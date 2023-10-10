from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Model object - single Student Data

def student_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

def student_List(request, pk):
    stu = Student.objects.get(id =pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

