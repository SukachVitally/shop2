from rest_framework import serializers
from shop.models import Product, ProductGroup, ProductInfo, ProductInfoType


class ProductGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductGroup
        fields = ('id', 'name')


class ProductInfoTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInfoType
        fields = ('id', 'name')


class ProductInfoSerializer(serializers.ModelSerializer):
    type = ProductInfoTypeSerializer()

    class Meta:
        model = ProductInfo
        fields = ('content', 'type')


class ProductBaseSerializer(serializers.ModelSerializer):
    groups = ProductGroupSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'groups')


class ProductFullSerializer(serializers.ModelSerializer):
    groups = ProductGroupSerializer(many=True)
    info = ProductInfoSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'groups', 'info')
