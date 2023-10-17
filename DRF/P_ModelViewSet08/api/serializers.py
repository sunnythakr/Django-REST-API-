from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = ['id','name','roll', 'city']

    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)