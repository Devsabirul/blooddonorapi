from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'is_admin', 'is_donor', 'date_joined', 'last_login', 'is_available')


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'is_admin', 'is_donor', 'date_joined', 'last_login', 'is_available')


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_Kwargs = {
            'password': {'write_only': True}
        }

        def validate(self, attrs):
            return super().validate(attrs)
