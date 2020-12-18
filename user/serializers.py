from rest_framework import serializers
from .models import User, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
