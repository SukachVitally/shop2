from rest_framework import serializers
from shop.models import Product, ProductGroup


class ProductGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductGroup
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    group = ProductGroupSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'group')

