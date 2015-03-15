from rest_framework import generics

from shop.models import Product
from shop.serializers import ProductBaseSerializer, ProductFullSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductBaseSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
