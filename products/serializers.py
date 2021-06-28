from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Product, Category


class CategorySerializers(serializers.ModelSerializer):
    class meta:
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ReadProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
