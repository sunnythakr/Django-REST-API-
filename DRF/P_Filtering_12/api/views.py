from django.shortcuts import render
from .serializers import StudentSerilizer
from .models import Student
from rest_framework.generics import ListAPIView

# Create your views here.
class StudntList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizer