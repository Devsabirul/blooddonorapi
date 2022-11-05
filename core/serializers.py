from rest_framework import serializers
from .models import *


class BloodDonorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorRegister
        fields = '__all__'
