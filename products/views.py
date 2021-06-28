
from rest_framework.views import APIView
from products.models import Category, Product
from rest_framework import (
    serializers,
    viewsets,
    status,
)
from django.core import paginator
from rest_framework.pagination import PageNumberPagination
import time
from .serializers import CategorySerializers, ProductSerializers, ReadProductSerializer

from rest_framework.response import Response

from django.core.cache import cache


class CustomPagination(PageNumberPagination):
    page_size = 10


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = CategorySerializers(Category.objects.all(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None,):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializers(category)

        return Response(
            serializer.data
        )

    def update(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializers(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ProductListApiView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10

        products = cache.get('products_data')

        if not products:
            time.sleep(5)
            products = list(Product.objects.select_related('category'))
            cache.set('products_data', products, timeout=60 * 30)

        result = paginator.paginate_queryset(products, request)

        serializer = ReadProductSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        for key in cache.keys('*'):
            if 'products_data' in key:
                cache.delete(key)
        cache.delete("products_data")

        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None,):
        products = Product.objects.get(id=pk)
        serializer = ReadProductSerializer(products)

        return Response(
            serializer.data
        )

    def update(self, request, pk=None):
        products = Product.objects.get(id=pk)
        serializer = ProductSerializers(
            instance=products, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        for key in cache.keys('*'):
            if 'products_data' in key:
                cache.delete(key)
        cache.delete("products_data")
        return Response(
            serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        products = Product.objects.get(id=pk)
        products.delete()
        for key in cache.keys('*'):
            if 'products_data' in key:
                cache.delete(key)
        cache.delete("products_data")
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
