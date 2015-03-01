from main.models import Product
from api.serializers import ProductSerializer
from rest_framework import generics


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
