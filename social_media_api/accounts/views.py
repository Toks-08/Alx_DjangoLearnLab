from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework import status

from django.shortcuts import redirect

# Create your views here.
class RegisterView(CreateAPIView):
    model = CustomUser
    serializer_class = RegistrationSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message':"Login Successful",
            'token': token.key,
            'user':{
                'id':user.id,
                'username': user.username,
                'email': user.email
            }

        }, status = status.HTTP_200_OK)

class ProfileView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UpdateProfileView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user



