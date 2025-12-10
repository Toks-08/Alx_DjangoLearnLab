from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs ['password'] != attrs ['password2']:
            raise serializers.ValidationError ("Password Must Be The Same")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required= True, write_only=True)

    def validate(self, validated_data):
        user = authenticate(**validated_data)
        if not user:
            raise serializers.ValidationError("Invalid Username Or Password")
        validated_data['user'] = user
        return validated_data

class CustomUserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True )
    following = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.all()
    )
    class Meta:
        model = CustomUser
        fields = ['id', 'bio', 'profile_picture', 'followers']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'email']

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name']

