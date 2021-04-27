from rest_framework import serializers
from . import models

class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'
