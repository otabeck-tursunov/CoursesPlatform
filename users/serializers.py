from rest_framework import serializers
from .models import Student


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'password', 'email', 'phone_number', 'first_name', 'last_name')

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'username', 'email', 'first_name', 'last_name', 'role', 'point', 'birth_date', 'date_joined',
            'last_login'
        )


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'birth_date')
        extra_kwargs = {
            'username': {'required': False},
            'password': {'required': False},
            'email': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'birth_date': {'required': False},
        }
