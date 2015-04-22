from rest_framework import generics

from shop.models import Product, ProductGroup
from shop.serializers import ProductBaseSerializer, ProductFullSerializer, ProductGroupSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductBaseSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


class GroupList(generics.ListAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer