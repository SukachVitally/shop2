from rest_framework import generics

from shop.models import Product
from shop.serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
