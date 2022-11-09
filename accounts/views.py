from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *

# Generate Token manually


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


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


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializers = UserRegistrationSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            token = get_tokens_for_user(user)
            return Response({'status': 'success', 'token': token, 'msg': 'Account created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'errors': serializers.errors}, status=status.HTTP_409_CONFLICT)


class UserLoginApiView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            print(email, password)
            user = authenticate(request, email=email, password=password)
            print(user)
            return Response({'status': 'success', 'msg': 'Login success'}, status=status.HTTP_200_OK)
            # return Response({'status': 'failed', 'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
