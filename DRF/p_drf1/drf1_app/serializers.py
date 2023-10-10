from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name =serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

# deserialization function
class StudentDeserializer(serializers.Serializer):
    name =serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

from .models import Student
def create(self, validate_data):
    return Student.objects.create(**validate_data)