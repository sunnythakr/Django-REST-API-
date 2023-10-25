from .models import Student
from rest_framework import serializers

class StudentSerilizer(serializers.Serializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city', 'passby']