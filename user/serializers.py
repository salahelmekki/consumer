from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'last_name', 'first_name', 'pays', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data["role"] = "CUSTOMER"
        return User.objects.create(**validated_data)

    @staticmethod
    def validate_password(value: str) -> str:
        return make_password(value)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["role"] = user.role
        # ...

        return token
