from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'is_admin', 'is_donor', 'last_login', 'is_available')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'password2', 'is_donor', 'is_available')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializer.ValidationError(
                "Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)
        # Validating Password and Confirm Password while Registration

        def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.pop('password2')
            if password != password2:
                raise serializers.ValidationsError(
                    "Password and confirm Password doesn't match ")
            return attrs

        def create(self, validate_data):
            return CustomUser.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
