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

# deserialization function start here 
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentDeserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentDeserializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created '}
            json_data  = JSONRenderer().render(res)
            return HttpResponse(json_data, content='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content='application/json')

# CRUD functionality 
import io
from .serializers import CRUDSerializer
def CRUD_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = CRUDSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content='application/json')

        stu = Student.objects.all()
        serializer = CRUDSerializer().render(serializer.data)
        return HttpResponse(json_data,content='application/json')   