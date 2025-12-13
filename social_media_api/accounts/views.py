from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes

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
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    #user being followed
    user_to_follow = get_object_or_404(CustomUser, pk=user_id)

    #current user (the one performing the follow)
    current_user = request.user
    #prevent user from following themselves
    if current_user == user_to_follow:
        return Response({"details": "you cannot follow yourself"}, status = status.HTTP_400_BAD_REQUEST)
    # add user_to_follow to the current user following list
    current_user.following.add(user_to_follow)
    return Response ({
        "details":"user followed successfully"
    }, status = status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    #user being unfollowed
    user_to_unfollow = get_object_or_404(CustomUser, pk=user_id)
    #the current user performing the unfollow
    current_user = request.user
    #remove the user_to_follow from the current user following list
    current_user.following.remove(user_to_unfollow)
    return Response ({
        "details":"user unfollowed successfully"
    }, status = status.HTTP_200_OK)