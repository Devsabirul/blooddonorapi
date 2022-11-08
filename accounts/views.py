from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib import auth
from .models import *
from .serializers import *


class AccountsApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            account = CustomUser.objects.get(pk=id)
            serializers = UserSerializer(account)
            return Response({'status': 'success', "account": serializers.data}, status=200)
        account = CustomUser.objects.all()
        serializers = UserSerializer(account, many=True)
        return Response({'status': 'success', "account": serializers.data}, status=200)


'''
    def put(self, request, pk, format=None):
        id = pk
        account = CustomUser.objects.get(pk=id)
        serializer = UserSerializer(
            account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', "msg": "Data Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        account = CustomUser.objects.get(pk=id)
        serializer = UserSerializer(
            account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', "msg": "Data Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        account = CustomUser.objects.get(pk=id)
        account.delete()
        return Response({'status': 'success', "msg": "Data Deleted"})

'''


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializers = UserRegistrationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'success', 'msg': 'Account created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'errors': 'something wrong'}, status=status.HTTP_409_CONFLICT)


class UserLoginApiView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            print(email, password)
            return Response({'status': 'success', 'msg': 'Login success'}, status=status.HTTP_200_OK)
