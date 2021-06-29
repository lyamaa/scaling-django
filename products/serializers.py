from rest_framework import serializers

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

    # category = serializers.StringRelatedField(read_only=True)
    category = CategoryRelatedField()
    # category = CategorySerializers()
    # category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
