from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
         model = Profile
         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','email', 'username', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields do nt match."})
        password = attrs.get('password1', '')
        if len(password) < 8:
            raise serializers.ValidationError("password must be at least 8 character long")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")
        return User.objects.create_user(password=password, **validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("incorrect credentials")