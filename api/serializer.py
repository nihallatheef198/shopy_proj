from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from . import models

class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'

class user_serializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'is_admin']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name
    
    def get__id(self, obj):
        return obj.id 
    
    def get_is_admin(self, obj):
        return obj.is_staff

class user_serializer_token(user_serializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'is_admin', 'token'] 

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token) 