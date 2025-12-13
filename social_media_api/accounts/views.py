from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView

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


class FollowUserView(GenericAPIView):
    # Set the permission requirement for all users accessing this view
    permission_classes = [permissions.IsAuthenticated]

    # Note: We expect the user_id to be passed via the URL, so we use
    # the POST method to execute the action.
    def post(self, request, user_id, *args, **kwargs):
        # 1. Get the user to be followed
        user_to_follow = get_object_or_404(CustomUser, pk=user_id)
        current_user = request.user

        # 2. Check for self-following
        if current_user == user_to_follow:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 3. Add the follow relationship
        current_user.following.add(user_to_follow)

        return Response(
            {"detail": f"Now following {user_to_follow.username}."},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # 1. Get the user to be unfollowed
        user_to_unfollow = get_object_or_404(CustomUser, pk=user_id)
        current_user = request.user

        # 2. Remove the follow relationship
        current_user.following.remove(user_to_unfollow)

        return Response(
            {"detail": f"No longer following {user_to_unfollow.username}."},
            status=status.HTTP_200_OK
        )