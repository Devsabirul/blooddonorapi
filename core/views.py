from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.


def home(request):
    obj = DonorRegister.objects.order_by("-id")
    return render(request, "home/index.html", {'contents': obj})


# BloodDonorRegisterApiView api
class BloodDonorRegisterApiView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            BloodDonor = DonorRegister.objects.get(pk=id)
            serializers = BloodDonorRegisterSerializer(BloodDonor)
            return Response({'status': 'success', "bloodDonor": serializers.data}, status=200)
        BloodDonor = DonorRegister.objects.all()
        serializers = BloodDonorRegisterSerializer(BloodDonor, many=True)
        return Response({'status': 'success', "bloodDonor": serializers.data}, status=200)

    def post(self, request, format=None):
        serializers = BloodDonorRegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'success', "bloodDonor": serializers.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        BloodDonor = DonorRegister.objects.get(pk=id)
        serializer = BloodDonorRegisterSerializer(
            BloodDonor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', "msg": "Data Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        BloodDonor = DonorRegister.objects.get(pk=id)
        serializer = BloodDonorRegisterSerializer(
            BloodDonor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', "msg": "Data Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        BloodDonor = DonorRegister.objects.get(pk=id)
        BloodDonor.delete()
        return Response({'status': 'success', "msg": "Data Deleted"})
