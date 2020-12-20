from rest_framework import serializers
from .models import User, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['number', 'area_code', 'country_code']


class UserSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phones']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

