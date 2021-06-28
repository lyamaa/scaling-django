
from django.urls import path

from .views import ProductListApiView, ProductViewSet, CategoryViewSet

urlpatterns = [
    path("category", CategoryViewSet.as_view(
         {"get": "list", "post": "create"})),
    path(
        "category/<str:pk>",
        CategoryViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path('products', ProductListApiView.as_view()),

    path("product", ProductViewSet.as_view(
        {"post": "create"})),
    path(
        "product/<str:pk>",
        ProductViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
