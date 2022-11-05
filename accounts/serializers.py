from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'is_admin', 'is_donor', 'date_joined', 'last_login', 'is_available')
