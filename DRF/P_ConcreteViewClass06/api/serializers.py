from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = ['id','name','roll', 'city']

    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)