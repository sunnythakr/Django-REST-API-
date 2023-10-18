# ViewSet in Django REST framework
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Employee

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication # import authentication library 
from rest_framework.permissions import IsAuthenticated # import authentication library 
class EmployeeReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication] # authentication class
    permission_classes = [IsAuthenticated]



