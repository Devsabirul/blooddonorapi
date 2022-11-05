from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *


class RegisterApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            account = CustomUser.objects.get(pk=id)
            serializers = UserSerializer(account)
            return Response({'status': 'success', "account": serializers.data}, status=200)
        account = CustomUser.objects.all()
        serializers = UserSerializer(account, many=True)
        return Response({'status': 'success', "account": serializers.data}, status=200)

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'Account created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        account = CustomUser.objects.get(pk=id)
        serializer = UserSerializer(
            account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        account = CustomUser.objects.get(pk=id)
        serializer = UserSerializer(
            account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        account = CustomUser.objects.get(pk=id)
        account.delete()
        return Response({"msg": "Data Deleted"})