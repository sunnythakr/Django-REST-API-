# ViewSet in Django REST framework
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .custompermissions import MyPermission # import ccustompermissions
from .models import Employee

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication # import authentication library 
from rest_framework.permissions import IsAuthenticated # import authentication library 
class EmployeeReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication] # authentication class
    # permission_classes = [IsAuthenticated] # session Authentication
    permission_classes = [MyPermission] # Custom permission



