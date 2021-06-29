from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Product, Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return CategorySerializers(value).data

    def to_internal_value(self, data):
        return data


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ReadProductSerializer(serializers.ModelSerializer):

    category = StringRelatedField(read_only=True)
    # category = CategoryRelatedField()
    # category = CategorySerializers()

    class Meta:
        model = Product
        fields = "__all__"
