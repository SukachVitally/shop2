from rest_framework import serializers
from shop.models import Product, ProductGroup, ProductGroupRelation


class ProductGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductGroup
        fields = ('id', 'name')


class ProductGroupRelationSerializer(serializers.ModelSerializer):
    group = ProductGroupSerializer()

    class Meta:
        model = ProductGroupRelation
        fields = ('group', )


class ProductSerializer(serializers.ModelSerializer):
    groups = ProductGroupRelationSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'groups')

